import sys
import os

# Add parent directory (exercises/) so 'kflow' can be imported as a package
# __file__ -> pipelines/local_test.py -> kflow/pipelines -> kflow -> exercises
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# print(sys.path)

sys.path.insert(0, '.')

from data import prepare_data, train_test_split_data

if __name__ == "__main__":
    print("Starting local test...")
    print("Preparing data...")
    prepare_data('./test_data')
    print("Train/test split data...")
    train_test_split_data('./test_data')
    print("✅ Local test passed!")
    print("Local test completed!")