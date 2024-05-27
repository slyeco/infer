# flask_app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

received_data = []

@app.route('/receive', methods=['POST'])
def receive_json():
    data = request.json
    received_data.append(data)
    return jsonify({"status": "success", "received_data": data})

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(received_data)

if __name__ == '__main__':
    app.run(port=5000)
