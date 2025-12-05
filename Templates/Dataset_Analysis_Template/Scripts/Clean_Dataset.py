"""
Script: Clean Dataset
Purpose: Process raw data into analysis-ready format.
Author: AI Assistant / [User Name]
"""

import pandas as pd
import numpy as np
from Config import * # Imports all paths

def load_raw_data():
    """Load data from the raw directory with safety checks."""
    print(f"Loading raw data from: {RAW_DATA_PATH}...")
    if not RAW_DATA_PATH.exists():
        raise FileNotFoundError(f"❌ Critical Error: File not found at {RAW_DATA_PATH}")
    
    # Auto-detect filetype
    if RAW_DATA_PATH.suffix == '.csv':
        df = pd.read_csv(RAW_DATA_PATH)
    elif RAW_DATA_PATH.suffix in ['.xls', '.xlsx']:
        df = pd.read_excel(RAW_DATA_PATH)
    else:
        raise ValueError("Unsupported file format.")
    
    print(f"✅ Loaded {len(df)} rows.")
    return df

def clean_data(df):
    """
    Main cleaning logic.
    [AI INSTRUCTION]: Add specific cleaning steps here based on Data Inspection.
    """
    df_clean = df.copy()
    
    # Step 1: Standardize Column Names
    df_clean.columns = [c.strip().lower().replace(' ', '_') for c in df_clean.columns]
    
    # [Insert further cleaning steps here]
    
    return df_clean

def save_data(df):
    """Save processed data to the processed directory."""
    print(f"Saving processed data to: {CLEAN_DATA_PATH}...")
    df.to_csv(CLEAN_DATA_PATH, index=False)
    print("✅ Data saved successfully.")

if __name__ == "__main__":
    print("--- Starting Data Cleaning ---")
    raw_df = load_raw_data()
    clean_df = clean_data(raw_df)
    save_data(clean_df)
    print("--- Cleaning Complete ---")
