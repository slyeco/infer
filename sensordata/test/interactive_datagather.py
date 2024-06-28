#%% Part 1
# Install required libraries
!pip install influxdb-client pandas ipywidgets pytz

# Import necessary libraries
import pandas as pd
from influxdb_client import InfluxDBClient
from influxdb_client.client.exceptions import InfluxDBError
from datetime import datetime
import pytz
from IPython.display import display
import ipywidgets as widgets

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
def query_data(start, stop, devEui, field):
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
        records = []
        for table in tables:
            for record in table.records:
                records.append((record.get_time().astimezone(pytz.UTC), record.get_value()))
        df = pd.DataFrame(records, columns=["time", field])
        df.set_index("time", inplace=True)
        return df
    except InfluxDBError as e:
        print(f"Query exception: {e}")
        return pd.DataFrame()

# Create interactive widgets
sensor_widget = widgets.Dropdown(
    options={devEui: devEui for devEui in sum(sensor_categories.values(), [])},
    description='Sensor:',
    disabled=False
)
field_widget = widgets.Dropdown(
    options=['s0', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9'],
    description='Field:',
    disabled=False
)
start_date_widget = widgets.DatePicker(description='Start Date', disabled=False)
end_date_widget = widgets.DatePicker(description='End Date', disabled=False)

output = widgets.Output()

def on_button_clicked(b):
    devEui = sensor_widget.value
    field = field_widget.value
    start = pytz.utc.localize(datetime.combine(start_date_widget.value, datetime.min.time())).strftime('%Y-%m-%dT%H:%M:%SZ')
    stop = pytz.utc.localize(datetime.combine(end_date_widget.value, datetime.min.time())).strftime('%Y-%m-%dT%H:%M:%SZ')
    
    df = query_data(start, stop, devEui, field)
    if not df.empty:
        df.to_csv('queried_data.csv')
        with output:
            output.clear_output()
            display(df)
            print("Data saved to queried_data.csv")
    else:
        with output:
            output.clear_output()
            print("No data returned from the query.")

button = widgets.Button(description="Query Data")
button.on_click(on_button_clicked)

# Display widgets
display(sensor_widget, field_widget, start_date_widget, end_date_widget, button, output)


#%% Part 2
# Install required libraries
!pip install pandas ipywidgets bqplot

# Import necessary libraries
import pandas as pd
import ipywidgets as widgets
import bqplot as bq
from IPython.display import display

# Function to plot and interact with data
def interactive_plot(df, field):
    x_sc = bq.DateScale()
    y_sc = bq.LinearScale()
    
    line = bq.Lines(x=df.index, y=df[field], scales={'x': x_sc, 'y': y_sc})
    ax_x = bq.Axis(scale=x_sc, label='Time', tick_format='%H:%M')
    ax_y = bq.Axis(scale=y_sc, orientation='vertical', label='Value')
    
    fig = bq.Figure(marks=[line], axes=[ax_x, ax_y], title=f'{field} over time')
    
    selector = bq.interacts.BrushIntervalSelector(scale=x_sc, marks=[line])
    fig.interaction = selector
    
    display(fig)
    
    def on_selection_change(change):
        if change['new'] is not None and len(change['new']) == 2:
            start, end = change['new']
            selected_df = df[(df.index >= start) & (df.index <= end)]
            display(selected_df)
            selected_df.to_csv('selected_data.csv')
            print("Selected data saved to selected_data.csv")
    
    selector.observe(on_selection_change, names=['selected'])

# Load the stored data
df = pd.read_csv('queried_data.csv', index_col='time', parse_dates=True)
df.index = df.index.tz_convert('UTC')

# Select the field to visualize (must match the field used in querying)
field = df.columns[0]  # Assuming the field is the only column besides the index

# Plot and interact with the data
interactive_plot(df, field)
# %%
