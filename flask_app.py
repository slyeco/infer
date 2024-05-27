# flask_app.py
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

received_data = []

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/receive', methods=['POST'])
def receive_json():
    try:
        data = request.json
        if data is None:
            raise ValueError("No JSON data received")
        received_data.append(data)
        logger.info(f"Received data: {data}")
        return jsonify({"status": "success", "received_data": data}), 200
    except ValueError as ve:
        logger.error(f"ValueError: {ve}")
        return jsonify({"status": "error", "message": str(ve)}), 400
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({"status": "error", "message": "An unexpected error occurred"}), 500

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(received_data), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

