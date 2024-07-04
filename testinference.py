import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, accuracy_score
import os

def load_models(rf_model_path, xgb_model_path):
    """Load the trained models."""
    rf_model = joblib.load(rf_model_path)
    xgb_model = joblib.load(xgb_model_path)
    return rf_model, xgb_model

def preprocess_data(air_file_path, fire_file_path):
    """Load and preprocess the datasets, merging air and fire data."""
    air_data = pd.read_csv(air_file_path)
    fire_data = pd.read_csv(fire_file_path)
    
    air_data['label'] = 'air'
    fire_data['label'] = 'fire'
    
    data = pd.concat([air_data, fire_data], ignore_index=True)
    
    required_columns = [f'Resistance{i}' for i in range(10)] + ['label']
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        raise KeyError(f"Missing columns in dataset: {missing_columns}")

    for i in range(10):
        data[f's{i}'] = data[f'Resistance{i}']
    
    for i in range(10):
        data[f'log_s{i}'] = np.log10(data[f's{i}'] + 1)

    for i in range(9):
        data[f'D{i}'] = data[f'log_s{i+1}'] - data[f'log_s{i}']
    
    label_encoder = LabelEncoder()
    data['label_encoded'] = label_encoder.fit_transform(data['label'])
    
    # Ensure air = 0 and fire/smoke = 1
    label_mapping = dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))
    if label_mapping['air'] != 0 or label_mapping['fire'] != 1:
        raise ValueError("Label encoding mismatch: air should be 0 and fire/smoke should be 1")
    
    return data, label_encoder

def perform_inference(model, X):
    """Perform inference using the given model."""
    predictions = model.predict(X)
    return predictions

def train_new_models_with_inference_data(data, rf_model_path, xgb_model_path):
    """Train new models using the original and inference test data."""
    features = [f'D{i}' for i in range(9)]
    X = data[features]
    y = data['label_encoded']

    # Train and evaluate Random Forest model
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(X, y)
    y_pred_rf = rf_model.predict(X)
    print("Random Forest Classification Report (New Training):")
    print(classification_report(y, y_pred_rf))
    print("Random Forest Accuracy (New Training):", accuracy_score(y, y_pred_rf))

    # Save Random Forest model
    joblib.dump(rf_model, rf_model_path)
    print(f"Random Forest model (new training) saved to '{rf_model_path}'")

    # Train and evaluate XGBoost model
    xgb_model = XGBClassifier(random_state=42)
    xgb_model.fit(X, y)
    y_pred_xgb = xgb_model.predict(X)
    print("XGBoost Classification Report (New Training):")
    print(classification_report(y, y_pred_xgb))
    print("XGBoost Accuracy (New Training):", accuracy_score(y, y_pred_xgb))

    # Save XGBoost model
    joblib.dump(xgb_model, xgb_model_path)
    print(f"XGBoost model (new training) saved to '{xgb_model_path}'")

def main():
    # File paths
    rf_model_path = '/home/max/infer/sensordata/rf_model.joblib'
    xgb_model_path = '/home/max/infer/sensordata/xgb_model.joblib'
    air_file_path = '/home/max/infer/sensordata/air.csv'
    fire_file_path = '/home/max/infer/sensordata/fire.csv'

    # Load models
    rf_model, xgb_model = load_models(rf_model_path, xgb_model_path)

    # Load and preprocess the data
    try:
        data, label_encoder = preprocess_data(air_file_path, fire_file_path)
    except Exception as e:
        print(f"Error preprocessing data: {e}")
        return
    
    X = data[[f'D{i}' for i in range(9)]]
    y = data['label_encoded']

    # Perform inference
    y_pred_rf = perform_inference(rf_model, X)
    y_pred_xgb = perform_inference(xgb_model, X)

    # Analyze results
    print("Random Forest Classification Report:")
    print(classification_report(y, y_pred_rf))
    print("Random Forest Accuracy:", accuracy_score(y, y_pred_rf))

    print("XGBoost Classification Report:")
    print(classification_report(y, y_pred_xgb))
    print("XGBoost Accuracy:", accuracy_score(y, y_pred_xgb))

    # Uncomment the following section to retrain the models with the inference test data
    #"""
    # Paths for saving the newly trained models
    new_rf_model_path = '/home/max/infer/sensordata/rf_model_new.joblib'
    new_xgb_model_path = '/home/max/infer/sensordata/xgb_model_new.joblib'

    # Train new models with the combined data and test on the same combined data
    train_new_models_with_inference_data(data, new_rf_model_path, new_xgb_model_path)

    # Load and preprocess the data again for consistent test
    try:
        data, _ = preprocess_data(air_file_path, fire_file_path)
    except Exception as e:
        print(f"Error preprocessing data: {e}")
        return
    
    X = data[[f'D{i}' for i in range(9)]]
    y = data['label_encoded']

    # Load the newly trained models
    new_rf_model, new_xgb_model = load_models(new_rf_model_path, new_xgb_model_path)

    # Perform inference with the newly trained models
    y_pred_rf_new = perform_inference(new_rf_model, X)
    y_pred_xgb_new = perform_inference(new_xgb_model, X)

    # Analyze results for the new models
    print("New Random Forest Classification Report:")
    print(classification_report(y, y_pred_rf_new))
    print("New Random Forest Accuracy:", accuracy_score(y, y_pred_rf_new))

    print("New XGBoost Classification Report:")
    print(classification_report(y, y_pred_xgb_new))
    print("New XGBoost Accuracy:", accuracy_score(y, y_pred_xgb_new))
    #"""

if __name__ == "__main__":
    main()