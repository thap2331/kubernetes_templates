# ds_code/data_processing.py
"""Data Scientists write this - no Kubeflow dependencies needed"""
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split


def prepare_data(data_path: str):
    """Load and prepare iris dataset"""
    import os
    os.makedirs(data_path, exist_ok=True)
    
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    
    df = df.dropna()
    df.to_csv(f'{data_path}/final_df.csv', index=False)
    print(f"Data saved to {data_path}/final_df.csv")


def train_test_split_data(data_path: str):
    """Split data into train and test sets"""
    final_data = pd.read_csv(f'{data_path}/final_df.csv')
    
    target_column = 'species'
    X = final_data.loc[:, final_data.columns != target_column]
    y = final_data.loc[:, final_data.columns == target_column]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, stratify=y, random_state=47
    )
    
    np.save(f'{data_path}/X_train.npy', X_train)
    np.save(f'{data_path}/X_test.npy', X_test)
    np.save(f'{data_path}/y_train.npy', y_train)
    np.save(f'{data_path}/y_test.npy', y_test)
    print(f"Train/test split saved to {data_path}")