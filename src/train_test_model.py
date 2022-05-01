"""
Train model procedure
"""
from sklearn.model_selection import train_test_split
import pandas as pd
from joblib import dump
import src.help_functions


def train_test_model():
    """
    Execute model training
    """
    df = pd.read_csv("data/cleaned/census.csv")
    train, _ = train_test_split(df, test_size=0.20)

    X_train, y_train, encoder, lb = src.help_functions.process_data(
        train, categorical_features=src.help_functions.get_cat_features(),
        label="salary", training=True
    )
    trained_model = src.help_functions.train_model(X_train, y_train)

    dump(trained_model, "model/model.joblib")
    dump(encoder, "model/encoder.joblib")
    dump(lb, "model/lb.joblib")
