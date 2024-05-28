from flask import Flask, request, jsonify
from collections import deque
import joblib
import numpy as np
import json
import urllib.request
import logging
#rf
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay, classification_report
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint
#xg
import xgboost as xgb

app = Flask(__name__)

# Load pre-trained classifier
classifier = joblib.load('xg20d.joblib')

# Store only the last 10 messages
max_messages = 10
received_data = deque(maxlen=max_messages)

# Function to push inference data to Resiot
def resiot_http_push(appEUI, devEUI, name, value):
    base_url = "http://15.160.194.92:58089"
    token = "3cef9fccfdf0de6a48a679239e1bed0c"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": token
    }
    endpoint = f"{base_url}/api/application/{appEUI}/nodes/{devEUI}/tag/{name}/value"
    data = json.dumps({"value": value}).encode('utf-8')
    req = urllib.request.Request(endpoint, data=data, headers=headers, method="PUT")
    try:
        with urllib.request.urlopen(req) as response:
            response_body = response.read().decode()
            logging.info(f"Update for {name} was successful. Response: {response_body}")
    except urllib.error.HTTPError as e:
        logging.error(f"Update for {name} failed with status code {e.code}. Response: {e.read().decode()}")

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
        'vcc': data['nodetags'].get('vcc', {}).get('Value')
    }

    # Prepare the array for inference
    s_array = np.array([filtered_data['s0'], filtered_data['s1'], filtered_data['s2'], filtered_data['s3'],
                        filtered_data['s4'], filtered_data['s5'], filtered_data['s6'], filtered_data['s7'],
                        filtered_data['s8'], filtered_data['s9']], dtype=np.int64).reshape(1, -1)

    # Perform inference
    inference = classifier.predict(s_array)[0]
    print("inference: " + inference)
    # Add inference to the filtered data
    filtered_data['inference'] = inference

    # Push the inference to Resiot
    resiot_http_push('3a6e00000000aaaa', filtered_data['deveui'], 'smk', inference)

    received_data.append(filtered_data)
    return jsonify({"status": "success", "received_data": filtered_data})

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(list(received_data))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
