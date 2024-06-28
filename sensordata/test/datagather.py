# Install required libraries
#pip install influxdb-client pandas matplotlib ipywidgets scikit-learn

#%% Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from influxdb_client import InfluxDBClient
from influxdb_client.client.exceptions import InfluxDBError
from datetime import datetime
from IPython.display import display
import ipywidgets as widgets
import numpy as np

# Setup InfluxDB client
token = "4P2zD5Vc79EP40QdMbUcNR7Wor6s2JlUSz44MSjlJtBGL_5AFC78nwWwSkiTwzXD22pG-vJWu5R8AocA8ZBAmw=="
org = "sly"
bucket = "resiot"
url = "http://ec2-15-160-116-77.eu-south-1.compute.amazonaws.com:8086"

client = InfluxDBClient(url=url, token=token, org=org)

# Define sensor categories
sensor_categories = {
    'Indoor': ['3a6e00000000a001', '3a6e00000000a002', '3a6e00000000a005', '3a6e00000000a006', '3a6e00000000a038', '3a6e00000000a039'],
    'Sputnik': ['3a6e00000000a003', '3a6e00000000a004'],
    'Outdoor': ['3a6e00000000a026', '3a6e00000000a027', '3a6e00000000a028', '3a6e00000000a029', '3a6e00000000a030', '3a6e00000000a031',
                '3a6e00000000a032', '3a6e00000000a033', '3a6e00000000a034', '3a6e00000000a035', '3a6e00000000a036', '3a6e00000000a037', '3a6e00000000a040'],
    'Outdoor SPS': ['3a6e00000000a010', '3a6e00000000a011', '3a6e00000000a012', '3a6e00000000a013', '3a6e00000000a014', '3a6e00000000a015',
                    '3a6e00000000a016', '3a6e00000000a017', '3a6e00000000a018', '3a6e00000000a019', '3a6e00000000a020', '3a6e00000000a021',
                    '3a6e00000000a022', '3a6e00000000a023', '3a6e00000000a024', '3a6e00000000a025']
}

# Define a function to query data
def query_data(start, stop, devEui):
    data = []
    fields = ['s0', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9']
    for field in fields:
        query = f'''
        from(bucket: "{bucket}")
          |> range(start: {start}, stop: {stop})
          |> filter(fn: (r) => r["devEui"] == "{devEui}")
          |> filter(fn: (r) => r["_field"] == "{field}")
          |> aggregateWindow(every: 1m, fn: mean, createEmpty: false)
          |> yield(name: "mean")
        '''
        try:
            tables = client.query_api().query(query, org=org)
            data.append((tables, field))
        except InfluxDBError as e:
            print(f"Query exception for field {field}: {e}")
    return data

# Define a function to process and visualize the data
def visualize_data(tables_list, devEui):
    if not tables_list:
        print("No data returned from the query.")
        return

    data = {}
    for tables, field in tables_list:
        records = []
        for table in tables:
            for record in table.records:
                record_dict = record.values
                records.append(record_dict)

        df = pd.DataFrame(records)
        df.set_index("_time", inplace=True)
        df.index = pd.to_datetime(df.index)
        data[field] = df["_value"]

    combined_df = pd.concat(data, axis=1).dropna()

    plt.figure(figsize=(12, 8))
    for field in data.keys():
        plt.plot(combined_df.index, combined_df[field], linestyle='-', label=f'{devEui} {field}')

    plt.title('Data Visualization for Selected Sensors')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.yscale('log')
    plt.legend()
    plt.grid()
    plt.show()

    return combined_df

# Function to export data to CSV
def export_to_csv(dataframe, devEui):
    filename = f"sensor_data_{devEui}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    dataframe.to_csv(filename)
    print(f"Data exported to {filename}")

# Create interactive widgets
category_widget = widgets.Dropdown(
    options=list(sensor_categories.keys()),
    description='Category:',
    disabled=False
)

devEui_widget = widgets.SelectMultiple(
    options=sensor_categories[category_widget.value],
    description='devEui:',
    disabled=False
)
start_date_widget = widgets.DatePicker(description='Start Date', disabled=False)
end_date_widget = widgets.DatePicker(description='End Date', disabled=False)

# Update devEui options based on selected category
def update_sensors(*args):
    devEui_widget.options = sensor_categories[category_widget.value]

category_widget.observe(update_sensors, 'value')

def on_button_clicked(b):
    start = start_date_widget.value.strftime('%Y-%m-%dT%H:%M:%SZ')
    stop = end_date_widget.value.strftime('%Y-%m-%dT%H:%M:%SZ')
    
    for devEui in devEui_widget.value:
        tables_list = query_data(start, stop, devEui)
        df = visualize_data(tables_list, devEui)
        display(df)
        export_to_csv(df, devEui)

button = widgets.Button(description="Query Data")
button.on_click(on_button_clicked)

# Display widgets
display(category_widget, devEui_widget, start_date_widget, end_date_widget, button)

# %%
