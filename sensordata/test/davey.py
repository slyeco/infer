#%% Setup
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from influxdb_client import InfluxDBClient

# InfluxDB configuration
bucket = "resiot"
org = "sly"
token = "4P2zD5Vc79EP40QdMbUcNR7Wor6s2JlUSz44MSjlJtBGL_5AFC78nwWwSkiTwzXD22pG-vJWu5R8AocA8ZBAmw=="
url = "http://ec2-15-160-116-77.eu-south-1.compute.amazonaws.com:8086"

# InfluxDB connection
client = InfluxDBClient(url=url, token=token, org=org)
query_api = client.query_api()

#%% Begin and End
start_date = "2024-06-12T05:36:51+02:00"
end_date = "2024-06-15T23:59:59+02:00"

# Query
query = f'''
from(bucket: "{bucket}")
|> range(start: {start_date}, stop: {end_date})
|> filter(fn: (r) => r._measurement == "sensor_data")
|> filter(fn: (r) => r.devEui == "3a6e00000000a009")
|> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
|> keep(columns: ["_time", "tmp", "hum", "pre", "vcc", "vpa", "s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9"])
'''
result = query_api.query_data_frame(query)
data = result.dropna()

#%% Step 3: Modify the time axis
data['Date'] = pd.to_datetime(data['_time']).dt.tz_localize(None)  # Remove timezone
data['Time'] = (data['Date'] - data['Date'].iloc[0]).dt.total_seconds()

# Step 4: Filter the data based on `vcc`
data['vcc'] = data['vcc'].astype(float)
vcc_min = data['vcc'].min()
vcc_max = data['vcc'].max()
vcc_threshold = vcc_min + (vcc_max - vcc_min) * 0.05
filtered_data = data[data['vcc'] >= vcc_threshold]

# Step 5: Handle time intervals to remove
gaps = np.diff(filtered_data['Time'])
long_gaps_indices = np.where(gaps > 1200)[0]  # 1200 seconds = 20 minutes
times_to_remove = []
for index in long_gaps_indices:
    end_time = filtered_data['Time'].iloc[index]
    times_to_remove.append((end_time, end_time + 1800))  # 1800 seconds = 30 minutes
for start, end in times_to_remove:
    filtered_data = filtered_data[(filtered_data['Time'] < start) | (filtered_data['Time'] > end)]

# Step 6: Identify reactivation points and remove subsequent 30 minutes of data
data['vcc_derivative'] = data['vcc'].diff()
vcc_reactivation_threshold = 0.01  # Define an appropriate threshold
reactivation_points = data[data['vcc_derivative'] > vcc_reactivation_threshold]['Time']
for point in reactivation_points:
    end_time = point + 1800  # 1800 seconds = 30 minutes
    filtered_data = filtered_data[(filtered_data['Time'] < point) | (filtered_data['Time'] > end_time)]

# Step 7: Calculate mean values for `s0` to `s9` based on `tmp` and `hum`
filtered_data['tmp'] = filtered_data['tmp'].astype(float)
filtered_data['hum'] = filtered_data['hum'].astype(float)
selected_data = filtered_data[(filtered_data['tmp'] > 24.8) & (filtered_data['tmp'] < 25.2) &
                              (filtered_data['hum'] > 48) & (filtered_data['hum'] < 52)]
mean_values = selected_data[['s0', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9']].mean()

# Step 8: Polynomial regression to remove the effect of temperature and humidity
def polynomial_regression(df, feature, mean_value):
    X = df[['tmp', 'hum']]
    y = df[feature].astype(float)
    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(X)
    model = LinearRegression()
    model.fit(X_poly, y)
    y_pred = model.predict(X_poly)
    residuals = y - y_pred
    adjusted = residuals + mean_value
    return adjusted
for feature in ['s0', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9']:
    filtered_data[feature] = polynomial_regression(filtered_data, feature, mean_values[feature])

# Step 9: Save the compensated data to a CSV file
output_file = '/home/max/infer/sensordata/test/compensated_data.csv'
filtered_data.to_csv(output_file, index=False)

# Step 10: Plot the data before and after compensation
fig, axs = plt.subplots(10, 1, figsize=(14, 20), sharex=True)
for i, feature in enumerate(['s0', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9']):
    original_data = data[['Time', feature]].dropna()
    compensated_data = filtered_data[['Time', feature]]
    axs[i].plot(original_data['Time'], original_data[feature], label=f'Original {feature}')
    axs[i].plot(compensated_data['Time'], compensated_data[feature], label=f'Compensated {feature}', color='orange')
    axs[i].set_ylabel(feature)
    axs[i].legend()
plt.xlabel('Time (seconds)')
plt.tight_layout()
plt.show()