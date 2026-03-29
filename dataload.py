import pandas as pd
import numpy as np

def load_data(path):
    df = pd.read_csv(path)
    print("Shape:", df.shape)
    print("Columns:", df.columns)
    print("Data Types:\n", df.dtypes)
    print(df.head())
    print("Info",df.info())
    #Generate Summary Statistics
    print(df.describe())   # numerical data
    print(df.describe(include='object')) #Categorical data'''
    return df

