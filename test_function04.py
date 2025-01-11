import pandas as pd
import numpy as np
import os

file_path  = 'D:\\Python\\Python Test Code\\Employee Sample Data.xlsx'
def load_excel(file_path):
    """Load an Excel file into a DataFrame."""
    try:
        return pd.read_excel(file_path)
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

df = load_excel(file_path)

if df is not None:
    try:
        selected_columns = df[['Department', 'Age', 'Annual Salary']]
        selected_columns = selected_columns[selected_columns['Age'] >= 40]
        print(selected_columns)
    except KeyError as e:
        print(f"Error: {e}")
