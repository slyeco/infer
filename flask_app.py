from flask import Flask, request, jsonify
from collections import deque
import joblib
import numpy as np
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import json
import urllib.request
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

app = Flask(__name__)

# Store only the last 10 messages
max_messages = 10
received_data = deque(maxlen=max_messages)

# Load the model
model_file_path = 'sensordata/rf_model_new.joblib'
model = joblib.load(model_file_path)

# Email alert configuration
EMAIL_ADDRESS = 'sly@sly.eco'
EMAIL_PASSWORD = 'zypa rmea xpjp rura'
ALERT_RECIPIENTS = ['max@sly.eco', 'davide@sly.eco']
ALERT_THRESHOLD = 12.5
ALERT_COOLDOWN = timedelta(minutes=30)
last_alert_time = datetime.min
sensor_last_alert_times = {}

# ResIOT configuration
appEUI = "3A6E00000000AAAA"
resiot_base_url = "http://15.160.194.92:58089"
resiot_token = "3cef9fccfdf0de6a48a679239e1bed0c"
resiot_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": resiot_token
}

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
write_api = client.write_api(write_options=SYNCHRONOUS)

def send_email_alert(pm2e5_value, deveui):
    global sensor_last_alert_times
    current_time = datetime.now()
    last_sensor_alert = sensor_last_alert_times.get(deveui, datetime.min)  # Get last alert time for this sensor (default min if not found)
    
    if current_time - last_sensor_alert < timedelta(minutes=15):  # Check cooldown for this sensor
        print("Skipping alert due to cooldown period.")
        return  # Skip sending the alert if within cooldown period

    # Update last alert time for the sensor
    sensor_last_alert_times[deveui] = current_time
    
    msg = MIMEText(f"Alert: pm2e5 value exceeded threshold for sensor {deveui}! Current value: {pm2e5_value}")
    msg['Subject'] = 'PM2.5 Alert'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ", ".join(ALERT_RECIPIENTS)

    print("Preparing to send email...")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        print("Logged in to SMTP server.")
        server.sendmail(EMAIL_ADDRESS, ALERT_RECIPIENTS, msg.as_string())
        print("Email sent.")

def calculate_deltas(resistance_values):
    # Calculate the deltas as s1 - s0, s2 - s1, ..., s9 - s8
    deltas = [resistance_values[i+1] - resistance_values[i] for i in range(len(resistance_values) - 1)]
    return deltas

def predict_inference(model, resistance_values):
    deltas = calculate_deltas(resistance_values)
    
    input_array = np.array(deltas).reshape(1, -1)
    probabilities = model.predict_proba(input_array)
    return probabilities[0]  # return probabilities for the single input instance

def update_device_parameters(appEUI, devEUI, params_to_update):
    for name, value in params_to_update:
        endpoint = f"{resiot_base_url}/api/application/{appEUI}/nodes/{devEUI}/tag/{name}/value"
        data = json.dumps({"value": str(value) if value is not None else ""}).encode('utf-8')  # Convert the data to JSON and then to bytes
        
        # Create a request object
        req = urllib.request.Request(endpoint, data=data, headers=resiot_headers, method="PUT")
        
        try:
            # Send the request
            with urllib.request.urlopen(req) as response:
                response_body = response.read().decode()
                print(f"Update for {name} was successful. Response: {response_body}")
        except urllib.error.HTTPError as e:
            # Handle HTTP errors
            print(f"Update for {name} failed with status code {e.code}. Response: {e.read().decode()}")

def write_to_influxdb(devEui, appEui, smk_value):
    timestamp = datetime.utcnow()
    p = influxdb_client.Point("sensor_data") \
        .tag("devEui", devEui) \
        .tag("appEui", appEui) \
        .field("smk", smk_value) \
        .time(timestamp)
    write_api.write(bucket=bucket, org=org, record=p)
    print("Data written to InfluxDB successfully.")

@app.route('/receive', methods=['POST'])
def receive_json():
    data = request.json
    filtered_data = {
        'timestamp': data.get('DT'),
        'deveui': data.get('DevEui'),
        's0': data['nodetags'].get('s0', {}).get('Value'),
        's1': data['nodetags'].get('s1', {}).get('Value'),
        's2': data['nodetags'].get('s2', {}).get('Value'),
        's3': data['nodetags'].get('s3', {}).get('Value'),
        's4': data['nodetags'].get('s4', {}).get('Value'),
        's5': data['nodetags'].get('s5', {}).get('Value'),
        's6': data['nodetags'].get('s6', {}).get('Value'),
        's7': data['nodetags'].get('s7', {}).get('Value'),
        's8': data['nodetags'].get('s8', {}).get('Value'),
        's9': data['nodetags'].get('s9', {}).get('Value'),
        'tmp': data['nodetags'].get('tmp', {}).get('Value'),
        'hum': data['nodetags'].get('hum', {}).get('Value'),
        'pre': data['nodetags'].get('pre', {}).get('Value'),
        'vcc': data['nodetags'].get('vcc', {}).get('Value'),
        'pm2e5': data['nodetags'].get('pm2e5', {}).get('Value')
    }

    # Check pm2e5 value and send alert if necessary
    pm2e5_value = filtered_data.get('pm2e5')
    deveui = filtered_data.get('deveui')
    if pm2e5_value is not None and pm2e5_value > ALERT_THRESHOLD:
        send_email_alert(pm2e5_value, deveui)
    
    # Update smk parameter in ResIOT if pm2e5 value exceeds 15
    smk_value = 90 if pm2e5_value is not None and pm2e5_value > 15 else None
    update_device_parameters(appEUI, deveui, [('smk', smk_value)])

    # Write to InfluxDB
    write_to_influxdb(deveui, appEUI, smk_value if smk_value is not None else 0)

    # Get resistance values
    resistance_values = [
        filtered_data['s0'], filtered_data['s1'], filtered_data['s2'], filtered_data['s3'],
        filtered_data['s4'], filtered_data['s5'], filtered_data['s6'], filtered_data['s7'],
        filtered_data['s8'], filtered_data['s9']
    ]

    # Predict inference probability
    inference_probabilities = predict_inference(model, resistance_values)
    filtered_data['inference_probabilities'] = inference_probabilities.tolist()  # Convert to list for JSON serialization

    received_data.append(filtered_data)
    return jsonify({"status": "success", "received_data": filtered_data})

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(list(received_data))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)