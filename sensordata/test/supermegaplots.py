import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load the data
air_df = pd.read_csv('/home/max/infer/sensordata/air.csv')
fire_df = pd.read_csv('/home/max/infer/sensordata/fire.csv')

# Combine dataframes (assuming you want to combine them)
df = pd.concat([air_df, fire_df], ignore_index=True)

# Map Resistance0 to Resistance9 to s0 to s9
resistance_columns = [f'Resistance{i}' for i in range(10)]
renamed_columns = {f'Resistance{i}': f's{i}' for i in range(10)}
df.rename(columns=renamed_columns, inplace=True)

# Apply natural logarithm transformation to each s0, s1, ..., s9
for col in [f's{i}' for i in range(10)]:
    df[col] = df[col].apply(lambda x: np.log(x) if x > 0 else np.nan)

# Drop rows with NaN values resulting from log transformation
df.dropna(inplace=True)

#%%
# Plotting s0 vs Humidity
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['s0'], y=df['Humidity'])
plt.title('Relationship between s0 and Humidity')
plt.xlabel('s0 (log-transformed)')
plt.ylabel('Humidity')
plt.show()

# Linear regression and R^2
X_s0 = df[['s0']]
y_humidity = df['Humidity']
model_s0 = LinearRegression().fit(X_s0, y_humidity)
r2_s0 = model_s0.score(X_s0, y_humidity)
print(f"R^2 for s0 and Humidity: {r2_s0:.4f}")

#%%
# Calculating log ratio of s0 and s1
df['log_ratio_s0_s1'] = df['s0'] / df['s1']

# Plotting log ratio of s0 and s1 vs Humidity
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['log_ratio_s0_s1'], y=df['Humidity'])
plt.title('Relationship between Log Ratio of s0 and s1, and Humidity')
plt.xlabel('Log Ratio of s0 and s1')
plt.ylabel('Humidity')
plt.show()

# Linear regression and R^2
X_log_ratio = df[['log_ratio_s0_s1']]
model_log_ratio = LinearRegression().fit(X_log_ratio, y_humidity)
r2_log_ratio = model_log_ratio.score(X_log_ratio, y_humidity)
print(f"R^2 for Log Ratio of s0 and s1, and Humidity: {r2_log_ratio:.4f}")

#%%
# Residualizing s0 and s1
residuals = pd.DataFrame(index=df.index)
for col in ['s0', 's1']:
    # Fit linear regression model
    model = LinearRegression()
    model.fit(df[['Temperature', 'Humidity']], df[col])
    
    # Calculate residuals
    residuals[col] = df[col] - model.predict(df[['Temperature', 'Humidity']])

# Calculate the ratio of residuals
residuals['residual_log_ratio_s0_s1'] = residuals['s0'] / residuals['s1']

# Plotting residual log ratio of s0 and s1 vs Humidity
plt.figure(figsize=(10, 6))
sns.scatterplot(x=residuals['residual_log_ratio_s0_s1'], y=df['Humidity'])
plt.title('Relationship between Residual Log Ratio of s0 and s1, and Humidity')
plt.xlabel('Residual Log Ratio of s0 and s1')
plt.ylabel('Humidity')
plt.show()

# Linear regression and R^2
X_residual_log_ratio = residuals[['residual_log_ratio_s0_s1']]
model_residual_log_ratio = LinearRegression().fit(X_residual_log_ratio, y_humidity)
r2_residual_log_ratio = model_residual_log_ratio.score(X_residual_log_ratio, y_humidity)
print(f"R^2 for Residual Log Ratio of s0 and s1, and Humidity: {r2_residual_log_ratio:.4f}")
