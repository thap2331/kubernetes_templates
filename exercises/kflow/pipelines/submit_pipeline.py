# ml_engineer/submit_pipeline.py
import kfp
from data_processing import iris_pipeline

# Connect to Kubeflow (adjust host if needed)
client = kfp.Client(host='http://localhost:8080')

# Submit pipeline
run = client.create_run_from_pipeline_func(
    iris_pipeline,
    arguments={'data_path': './data'},
    experiment_name='iris-experiment'
)

print(f"Pipeline submitted!")
print(f"Run ID: {run.run_id}")