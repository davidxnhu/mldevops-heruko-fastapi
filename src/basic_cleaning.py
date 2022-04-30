"""
Basic cleaning procedure
"""
import pandas as pd


def __clean_dataset(df):
    """
    Clean the dataset doing some stuff got from eda
    """
    df.replace({'?': None}, inplace=True)
    df.dropna(inplace=True)

    #not used in ML
    df.drop("fnlgt", axis="columns", inplace=True)
    df.drop("education-num", axis="columns", inplace=True)
    df.drop("capital-gain", axis="columns", inplace=True)
    df.drop("capital-loss", axis="columns", inplace=True)

    return df

def execute_cleaning():
    """
    Execute data cleaning
    """
    df = pd.read_csv("data/raw/census.csv", skipinitialspace=True)
    df = __clean_dataset(df)
    df.to_csv("data/cleaned/census.csv", index=False)
