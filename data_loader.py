import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

if "_name_" == "_main_":
    df = load_data("raw_healthcare_data.csv")
    print(df.head())