import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Load the data
air_df = pd.read_csv('/home/max/infer/sensordata/air.csv')
fire_df = pd.read_csv('/home/max/infer/sensordata/fire.csv')

# Combine dataframes (assuming you want to combine them)
df = pd.concat([air_df, fire_df], ignore_index=True)

# Map Resistance0 to Resistance9 to s0 to s9
resistance_columns = [f'Resistance{i}' for i in range(10)]
renamed_columns = {f'Resistance{i}': f's{i}' for i in range(10)}
df.rename(columns=renamed_columns, inplace=True)

# Check for required columns
if 's0' not in df.columns or 'Humidity' not in df.columns:
    raise ValueError("The DataFrame does not contain the required 's0' or 'Humidity' columns.")

# Plotting s0 (Resistance0) vs Humidity
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['s0'], y=df['Humidity'])
plt.title('Relationship between Resistance0 (s0) and Humidity')
plt.xlabel('Resistance0 (s0)')
plt.ylabel('Humidity')
plt.show()

# Linear regression and R^2
X_s0 = df[['s0']]
y_humidity = df['Humidity']
model_s0 = LinearRegression().fit(X_s0, y_humidity)
r2_s0 = model_s0.score(X_s0, y_humidity)

# Calculate correlation
correlation_s0_humidity = df['s0'].corr(df['Humidity'])

print(f"R^2 for Resistance0 (s0) and Humidity: {r2_s0:.4f}")
print(f"Correlation between Resistance0 (s0) and Humidity: {correlation_s0_humidity:.4f}")
