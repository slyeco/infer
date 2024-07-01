from flask import Flask, request, jsonify
from collections import deque
import joblib
import numpy as np

app = Flask(__name__)

# Store only the last 10 messages
max_messages = 10
received_data = deque(maxlen=max_messages)

# Load the model
model_file_path = 'sensordata/rf.joblib'
model = joblib.load(model_file_path)

def predict_inference(model, resistance_values):
    input_array = np.array(resistance_values).reshape(1, -1)
    probabilities = model.predict_proba(input_array)
    return probabilities[0]  # return probabilities for the single input instance

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