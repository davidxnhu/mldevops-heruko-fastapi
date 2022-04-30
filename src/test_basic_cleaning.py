"""
Basic cleaning module test
"""
import pandas as pd
import pytest
import basic_cleaning


@pytest.fixture
def data():
    """
    Get dataset
    """
    df = pd.read_csv("data/raw/census.csv", skipinitialspace=True)
    df = basic_cleaning.__clean_dataset(df)
    return df

def test_number_rows(data):
    """
    Data rows must be larger than zero
    """
    assert data.shape[0] > 0

def test_null(data):
    """
    Data is assumed to have no null values
    """
    assert data.shape == data.dropna().shape


def test_question_mark(data):
    """
    Data is assumed to have no question marks value
    """
    assert '?' not in data.values

