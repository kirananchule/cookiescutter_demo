import pandas as pd

# Function to load data from a CSV file into a pandas DataFrame
def load_data(file_path):
    return pd.read_csv(file_path)
