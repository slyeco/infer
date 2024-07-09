import requests
from datetime import datetime

# InfluxDB v2 configuration
url = 'http://ec2-15-160-116-77.eu-south-1.compute.amazonaws.com:8086/api/v2/write'
org = 'sly'
bucket = 'resiot'
precision = 'ms'
token = '4P2zD5Vc79EP40QdMbUcNR7Wor6s2JlUSz44MSjlJtBGL_5AFC78nwWwSkiTwzXD22pG-vJWu5R8AocA8ZBAmw=='

# Data
devEui = '3a6e00000000a040'
appEui = '3A6E00000000AAAA'
smk_value = 0.03
measurement = 'sensor_data'
timestamp = int(datetime.utcnow().timestamp())  # current time in seconds

# Prepare the fields and tags
fields = {
    'smk': smk_value
}
tags = {
    'devEui': devEui,
    'appEui': appEui
}

def format_line_protocol(measurement, fields, tags, timestamp):
    # Construct the line protocol string
    tag_string = ','.join([f"{key}={value}" for key, value in tags.items()])
    field_string = ','.join([f"{key}={value}" for key, value in fields.items()])
    line_protocol = f"{measurement},{tag_string} {field_string} {timestamp}"
    return line_protocol

def push_to_influxdb(url, token, data, org, bucket, precision):
    headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'text/plain'
    }
    params = {
        'org': org,
        'bucket': bucket,
        'precision': precision
    }
    response = requests.post(url, headers=headers, params=params, data=data)
    if response.status_code == 204:
        print("Data written successfully.")
    else:
        print(f"Failed to write data: {response.status_code}, {response.text}")

# Format the data
line_protocol_data = format_line_protocol(measurement, fields, tags, timestamp)
print(f"Line Protocol Data: {line_protocol_data}")

# Send the data
push_to_influxdb(url, token, line_protocol_data, org, bucket, precision)