import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report

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

# Ensure the columns s0 to s9, Temperature, and Humidity exist
expected_columns = [f's{i}' for i in range(10)] + ['Temperature', 'Humidity']
missing_columns = [col for col in expected_columns if col not in df.columns]

if missing_columns:
    raise ValueError(f"Missing columns in the DataFrame: {missing_columns}")

# Apply natural logarithm transformation to each s0, s1, ..., s9
for col in [f's{i}' for i in range(10)]:
    df[col] = df[col].apply(lambda x: np.log(x) if x > 0 else np.nan)

# Drop rows with NaN values resulting from log transformation
df.dropna(inplace=True)

# Residualize the resistance measurements
residuals = pd.DataFrame(index=df.index)
for col in [f's{i}' for i in range(10)]:
    # Fit linear regression model
    model = LinearRegression()
    model.fit(df[['Temperature', 'Humidity']], df[col])
    
    # Calculate residuals
    residuals[col] = df[col] - model.predict(df[['Temperature', 'Humidity']])

# Add the label column to the residuals dataframe
residuals['label'] = df['label']

# Calculate the ratios of the residuals
for i in range(9):
    residuals[f'ratio_s{i}_s{i+1}'] = residuals[f's{i}'] / residuals[f's{i+1}']

# Drop rows with NaN values resulting from ratio calculation
residuals.dropna(inplace=True)

# Export the residualized dataframe with ratios to a CSV file
residuals.to_csv('residualized_data_with_ratios.csv', index=False)

# Prepare the machine learning data
X = residuals[[f'ratio_s{i}_s{i+1}' for i in range(9)]]
y = residuals['label']

# Split the data into train, validation, and test sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Train a random forest classifier
rf_classifier = RandomForestClassifier(n_estimators=200, random_state=42)
rf_classifier.fit(X_train, y_train)

# Validate the model
y_val_pred = rf_classifier.predict(X_val)
print("Validation Results")
print(confusion_matrix(y_val, y_val_pred))
print(classification_report(y_val, y_val_pred))

# Test the model
y_test_pred = rf_classifier.predict(X_test)
print("Test Results")
print(confusion_matrix(y_test, y_test_pred))
print(classification_report(y_test, y_test_pred))
