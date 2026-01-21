# kflow/pipelines/pipeline_dev.py
from kfp import compiler, kubernetes
from kfp.dsl import component, pipeline
import kfp

# Shared volume configuration
PVC_NAME = "local-data-pvc"  # From local-storage.yaml
MOUNT_PATH = "/mnt/data"     # Absolute path in container

@component(
    packages_to_install=["pandas", "numpy", "scikit-learn"],
    base_image="python:3.9",
)
def prepare_data_component(data_path: str):
    # Inline code for faster development (no image building)
    import pandas as pd
    from sklearn import datasets
    import os
    print(f"Preparing data in {data_path}")
    
    os.makedirs(data_path, exist_ok=True)
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df = df.dropna()
    df.to_csv(f'{data_path}/final_df.csv', index=False)
    print("✅ Data prepared")

@component(
    packages_to_install=["pandas", "numpy", "scikit-learn"],
    base_image="python:3.9",
)
def train_test_split_component(data_path: str):
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    
    final_data = pd.read_csv(f'{data_path}/final_df.csv')
    print(f"Read data from csv: {final_data.head()}")
    target_column = 'species'
    X = final_data.loc[:, final_data.columns != target_column]
    y = final_data.loc[:, final_data.columns == target_column]
    print(f"Training a model with {X.shape[0]} rows and {X.shape[1]} columns")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, stratify=y, random_state=47
    )
    print(f"Saved train/test split to {data_path}")
    np.save(f'{data_path}/X_train.npy', X_train)
    np.save(f'{data_path}/X_test.npy', X_test)
    np.save(f'{data_path}/y_train.npy', y_train)
    np.save(f'{data_path}/y_test.npy', y_test)
    print("✅ Train/test split complete")

@pipeline(name="iris-pipeline-dev")
def iris_pipeline_dev(data_path: str = MOUNT_PATH):
    prepare_task = prepare_data_component(data_path=data_path)
    kubernetes.mount_pvc(prepare_task, pvc_name=PVC_NAME, mount_path=MOUNT_PATH)
    
    split_task = train_test_split_component(data_path=data_path)
    kubernetes.mount_pvc(split_task, pvc_name=PVC_NAME, mount_path=MOUNT_PATH)
    split_task.after(prepare_task)

if __name__ == "__main__":
    # For dev: just compile and submit
    kfp.compiler.Compiler().compile(iris_pipeline_dev, 'pipeline_dev.yaml')
    
    # Auto-submit to local Kubeflow
    client = kfp.Client(host='http://localhost:8080')
    run = client.create_run_from_pipeline_func(
        iris_pipeline_dev,
        arguments={'data_path': f'{MOUNT_PATH}'},
        experiment_name='dev-testing'
    )
    print(f"✅ Pipeline submitted: {run.run_id}")