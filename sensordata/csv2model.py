#%% Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import joblib
import argparse

#%% Section 1: Load Data
def load_data(air_file, fire_file):
    air_df = pd.read_csv(air_file)
    fire_df = pd.read_csv(fire_file)
    return pd.concat([air_df, fire_df], ignore_index=True)

# Section 2: Preprocess Data
def preprocess_data(df):
    # Extract resistance values and labels
    X = df[[f'Resistance{i}' for i in range(10)]].values
    y = df['label'].values
    return X, y

# Section 3: Split Data
def split_data(X, y):
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42, stratify=y)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp)
    return X_train, X_val, X_test, y_train, y_val, y_test

#%% Section 4: Train Model
def train_model(X_train, y_train):
    clf = RandomForestClassifier(n_estimators=20, random_state=42)
    clf.fit(X_train, y_train)
    return clf

#%% Section 5: Evaluate Model
def evaluate_model(clf, X_val, y_val, X_test, y_test):
    y_val_pred = clf.predict(X_val)
    y_test_pred = clf.predict(X_test)
    
    print("Validation Set Evaluation:")
    print(confusion_matrix(y_val, y_val_pred))
    print(classification_report(y_val, y_val_pred))
    
    print("Test Set Evaluation:")
    print(confusion_matrix(y_test, y_test_pred))
    print(classification_report(y_test, y_test_pred))

#%% Section 6: Save Model
def save_model(clf, output_file):
    joblib.dump(clf, output_file)
    print(f"Model saved to {output_file}")

#%% Section 7: Main Execution
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train a Random Forest Classifier on resistance data')
    parser.add_argument('air_file', type=str, help='/home/max/infer/sensordata/air.csv')
    parser.add_argument('fire_file', type=str, help='/home/max/infer/sensordata/fire.csv')
    parser.add_argument('output_file', type=str, help='/home/max/infer/models/rf.joblib')
    
    args = parser.parse_args()
    
    # Load data
    df = load_data(args.air_file, args.fire_file)
    
    # Preprocess data
    X, y = preprocess_data(df)
    
    # Split data
    X_train, X_val, X_test, y_train, y_val, y_test = split_data(X, y)
    
    # Train model
    clf = train_model(X_train, y_train)
    
    # Evaluate model
    evaluate_model(clf, X_val, y_val, X_test, y_test)
    
    # Save model
    save_model(clf, args.output_file)

# %%
