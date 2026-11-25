"""
This module loads a trained machine learning model and makes predictions on new data.
"""

# Import necessary libraries
import models
import pandas as pd
import joblib
from sklearn import set_config

set_config(transform_output="pandas")

MODEL_PATH = "models/pipeline_logreg.joblib"

def load_model(model_path: str):
    """Load a trained model from the specified file path."""
    model = joblib.load(model_path)
    return model

def predict(data, model=load_model(MODEL_PATH)):
    '''
    Data -> pandas DataFrame \\
    model -> default is "models/pipeline_logreg.joblib"
    '''

    prediction = model.predict(data)
    return prediction


if __name__ == "__main__":
    # Example usage
    model = load_model(MODEL_PATH)

    # Sample input data
    sample_data = pd.read_csv("data/sample_input.csv")

    # Run predictions
    predictions = predict(model, sample_data)
    print("Predictions:", predictions)
