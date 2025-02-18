import pandas as pd
from src.data_loader import load_data
from src.text_cleaner import clean_text
from src.deidentify import remove_pii

def preprocess_healthcare_data(file_path):
    df = load_data(file_path)
    
    # Clean doctor notes
    df["doctor_notes"] = df["doctor_notes"].apply(lambda x: clean_text(str(x)))
    
    # De-identify patient information
    df["doctor_notes"] = df["doctor_notes"].apply(lambda x: remove_pii(str(x)))
    
    return df

if "_name_" == "_main_":
    cleaned_df = preprocess_healthcare_data("data/raw_healthcare_data.csv")
    cleaned_df.to_csv("data/cleaned_healthcare_data.csv", index=False)
    print("Data cleaning completed. Saved as 'cleaned_healthcare_data.csv'")