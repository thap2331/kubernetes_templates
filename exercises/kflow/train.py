from kfp.dsl import component, pipeline
import kfp
from kfp import kubernetes

@component(
    packages_to_install=["pandas", "numpy", "scikit-learn"],
    base_image="python:3.9",
)
def training_basic_classifier(data_path: str):
    import pandas as pd
    import numpy as np
    import os
    from sklearn.linear_model import LogisticRegression
    
    X_train = np.load(f'{data_path}/X_train.npy',allow_pickle=True)
    y_train = np.load(f'{data_path}/y_train.npy',allow_pickle=True)
    
    classifier = LogisticRegression(max_iter=500)
    classifier.fit(X_train,y_train)
    import pickle
    with open(f'{data_path}/model.pkl', 'wb') as f:
        pickle.dump(classifier, f)