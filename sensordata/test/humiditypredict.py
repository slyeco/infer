import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import math

# Load the data
air_df = pd.read_csv('/home/max/infer/sensordata/air.csv')
fire_df = pd.read_csv('/home/max/infer/sensordata/fire.csv')

# Combine dataframes (assuming you want to combine them)
df = pd.concat([air_df, fire_df], ignore_index=True)

# Check the columns
print("Columns in the DataFrame:", df.columns)

# Map Resistance0 to Resistance9 to s0 to s9
resistance_columns = [f'Resistance{i}' for i in range(10)]
renamed_columns = {f'Resistance{i}': f's{i}' for i in range(10)}
df.rename(columns=renamed_columns, inplace=True)

# Ensure the columns s0 to s9 exist
expected_columns = [f's{i}' for i in range(10)]
missing_columns = [col for col in expected_columns if col not in df.columns]

if missing_columns:
    raise ValueError(f"Missing columns in the DataFrame: {missing_columns}")

# Apply natural logarithm transformation to each s0, s1, ..., s9
for col in expected_columns:
    df[col] = df[col].apply(lambda x: np.log(x) if x > 0 else np.nan)

# Add columns for the ratio of each s0 to s1, s1 to s2, ..., s8 to s9
for i in range(9):
    df[f'ratio_s{i}_s{i+1}'] = df[f's{i}'] / df[f's{i+1}']

# Drop rows with NaN values resulting from log transformation or ratio computation
df.dropna(inplace=True)

# Export the modified dataframe to a CSV file
df.to_csv('transformed_data.csv', index=False)

# Check if the Humidity column exists
if 'Humidity' not in df.columns:
    raise ValueError("The DataFrame does not contain a 'Humidity' column.")

# Prepare the machine learning data
X = df[[f'ratio_s{i}_s{i+1}' for i in range(9)]]
y = df['Humidity']

# Split the data into train, validation, and test sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Train a random forest regressor
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
rf_regressor.fit(X_train, y_train)

# Validate the model
y_val_pred = rf_regressor.predict(X_val)
print("Validation Results")
print(f"Mean Squared Error: {mean_squared_error(y_val, y_val_pred)}")
print(f"R^2 Score: {r2_score(y_val, y_val_pred)}")

# Test the model
y_test_pred = rf_regressor.predict(X_test)
print("Test Results")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_test_pred)}")
print(f"R^2 Score: {r2_score(y_test, y_test_pred)}")
