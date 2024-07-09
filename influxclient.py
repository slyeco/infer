import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime

# InfluxDB v2 configuration
bucket = "resiot"
org = "sly"
token = "4P2zD5Vc79EP40QdMbUcNR7Wor6s2JlUSz44MSjlJtBGL_5AFC78nwWwSkiTwzXD22pG-vJWu5R8AocA8ZBAmw=="
url = "http://ec2-15-160-116-77.eu-south-1.compute.amazonaws.com:8086"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)

# Write script
write_api = client.write_api(write_options=SYNCHRONOUS)

# Define the measurement, tags, and fields
measurement = "sensor_data"
devEui = "3a6e00000000a040"
appEui = "3A6E00000000AAAA"
smk_value = 0.03
timestamp = datetime.utcnow()

# Create a point object and write it to InfluxDB
p = influxdb_client.Point(measurement) \
    .tag("devEui", devEui) \
    .tag("appEui", appEui) \
    .field("smk", smk_value) \
    .time(timestamp)

write_api.write(bucket=bucket, org=org, record=p)
print("Data written successfully.")