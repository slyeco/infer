# flask_app.py
from flask import Flask, request, jsonify
from collections import deque

app = Flask(__name__)

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


# Store only the last 10 messages
max_messages = 10
received_data = deque(maxlen=max_messages)

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
    
    # Inference dummy
    inference = data['nodetags'].get('vcc', {}).get('Value')

    # Push the inference to Resiot
    resiot_http_push('3a6e00000000aaaa', filtered_data['deveui'], 'smk', inference)
    
    received_data.append(filtered_data)
    return jsonify({"status": "success", "received_data": filtered_data})

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(list(received_data))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)