import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
import os
import joblib

def load_data(file_path):
    """Load the dataset from a CSV file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    data = pd.read_csv(file_path, delimiter=';')
    return data

def check_columns(data, required_columns):
    """Check if required columns are in the dataframe."""
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        raise KeyError(f"Missing columns in dataset: {missing_columns}")

def generate_log_columns(data):
    """Generate log10(si) columns."""
    for i in range(10):
        col_name = f's{i}'
        if col_name in data.columns:
            data[f'log_{col_name}'] = np.log10(data[col_name] + 1)
        else:
            raise KeyError(f"Column '{col_name}' not found in the dataset")
    return data

def generate_difference_columns(data):
    """Generate D0, D1, ..., D8 columns."""
    for i in range(9):
        data[f'D{i}'] = data[f'log_s{i+1}'] - data[f'log_s{i}']
    return data

def encode_labels(data, column):
    """Encode categorical labels into numerical values."""
    label_encoder = LabelEncoder()
    data[f'{column}_encoded'] = label_encoder.fit_transform(data[column])
    return data

def main():
    # File path
    file_path = '/home/max/infer/sensordata/merged_dataset_sensors_yellowfire.csv'  # Modify with the correct file path

    # Load dataset
    try:
        data = load_data(file_path)
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # Check for required columns
    required_columns = [f's{i}' for i in range(10)] + ['value']
    try:
        check_columns(data, required_columns)
    except KeyError as e:
        print(e)
        return

    # Generate log columns
    try:
        data = generate_log_columns(data)
    except KeyError as e:
        print(e)
        return

    # Generate difference columns
    data = generate_difference_columns(data)

    # Encode labels
    try:
        data = encode_labels(data, 'value')
    except KeyError as e:
        print(e)
        return

    print("Nomi delle colonne del file CSV:", data.columns)
    print("Valori unici nella colonna 'value_encoded':", data['value_encoded'].unique())

    # Create feature matrix and target vector
    features = [f'D{i}' for i in range(9)]
    X = data[features]
    y = data['value_encoded']

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train and evaluate Random Forest model
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(X_train, y_train)
    y_pred_rf = rf_model.predict(X_test)
    print("Random Forest Classification Report:")
    print(classification_report(y_test, y_pred_rf))
    print("Random Forest Accuracy:", accuracy_score(y_test, y_pred_rf))

    # Save Random Forest model
    rf_model_path = '/home/max/infer/sensordata/rf_model.joblib'
    joblib.dump(rf_model, rf_model_path)
    print(f"Random Forest model saved to '{rf_model_path}'")

    # Train and evaluate XGBoost model
    xgb_model = XGBClassifier(random_state=42)
    xgb_model.fit(X_train, y_train)
    y_pred_xgb = xgb_model.predict(X_test)
    print("XGBoost Classification Report:")
    print(classification_report(y_test, y_pred_xgb))
    print("XGBoost Accuracy:", accuracy_score(y_test, y_pred_xgb))

    # Save XGBoost model
    xgb_model_path = '/home/max/infer/sensordata/xgb_model.joblib'
    joblib.dump(xgb_model, xgb_model_path)
    print(f"XGBoost model saved to '{xgb_model_path}'")

    # Save the new dataset to a CSV file
    output_file = '/home/max/infer/sensordata/new_dataset.csv'
    data.to_csv(output_file, index=False)
    print(f"File salvato come '{output_file}'")

if __name__ == "__main__":
    main()
