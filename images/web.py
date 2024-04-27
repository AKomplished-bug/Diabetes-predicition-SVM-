import numpy as np
import pandas as pd
from sklearn.utils.validation import check_array
from sklearn.svm import SVC
import streamlit as st


@st.cache_data()
def load_data():
    """This function returns the preprocessed data"""

    # Load the Diabetes dataset into DataFrame.
    df = pd.read_csv('diabetes.csv')

    # Perform feature and target split
    X = df[["FastingGlc","AfterGlc","BloodPressure","SkinThickness","Insulin", "BMI", "GeneticCorr", "Age"]].copy()
    y = df['Outcome'].copy()

    return df.copy(), X, y

def train_model(X, y):
    """This function trains the model and returns the model and model score"""
    # Ensure arrays are writable
    X = check_array(X, ensure_2d=True, allow_nd=True, force_all_finite=True, ensure_min_samples=2, ensure_min_features=2)
    y = check_array(y, ensure_2d=False, ensure_min_samples=2, ensure_min_features=1)

    # Create the model
    model = SVC(
            C=1.0, kernel='rbf', degree=3, gamma='scale',
            coef0=0.0, shrinking=True, probability=False,
            tol=0.001, cache_size=200, class_weight=None,
            verbose=False, max_iter=-1, decision_function_shape='ovr',
            break_ties=False, random_state=None
        )
    # Fit the data on model
    model.fit(X.copy(), y.copy())
    # Get the model score
    score = model.score(X, y)

    # Return the values
    return model, score

def predict(X, y, features):
    # Create copies of X and y
    X_copy = X.copy()
    y_copy = y.copy()
    
    # Get model and model score
    model, score = train_model(X_copy, y_copy)
    
    # Predict the value
    prediction = model.predict(np.array(features).reshape(1, -1))

    return prediction, score