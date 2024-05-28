import json
import urllib.request
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def resiot_http_push(appEUI, devEUI, name, value):
    base_url = "http://15.160.194.92:58089"
    token = "3cef9fccfdf0de6a48a679239e1bed0c"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": token
    }
    endpoint = f"{base_url}/api/application/{appEUI}/nodes/{devEUI}/tag/{name}/value"
    data = json.dumps({"value": str(value)}).encode('utf-8')  # Ensure the value is a string
    req = urllib.request.Request(endpoint, data=data, headers=headers, method="PUT")
    try:
        with urllib.request.urlopen(req) as response:
            response_body = response.read().decode()
            logging.info(f"Update for {name} was successful. Response: {response_body}")
    except urllib.error.HTTPError as e:
        logging.error(f"Update for {name} failed with status code {e.code}. Response: {e.read().decode()}")

def main():
    # Sample data simulating received JSON
    sample_data = {
        "DT": "2024-05-27T22:27:47.956314505+02:00",
        "DevEui": "3a6e00000000a031",
        "nodetags": {
            "s0": {"Value": 482300},
            "s1": {"Value": 65931500},
            "s2": {"Value": 62311300},
            "s3": {"Value": 58988200},
            "s4": {"Value": 4530900},
            "s5": {"Value": 4475200},
            "s6": {"Value": 4431700},
            "s7": {"Value": 493800},
            "s8": {"Value": 537300},
            "s9": {"Value": 573000},
            "tmp": {"Value": 16.91},
            "hum": {"Value": 73.6},
            "pre": {"Value": 999.61},
            "vcc": {"Value": 3.197}
        }
    }

    filtered_data = {
        'timestamp': sample_data.get('DT'),
        'deveui': sample_data.get('DevEui'),
        's0': sample_data['nodetags'].get('s0', {}).get('Value'),
        's1': sample_data['nodetags'].get('s1', {}).get('Value'),
        's2': sample_data['nodetags'].get('s2', {}).get('Value'),
        's3': sample_data['nodetags'].get('s3', {}).get('Value'),
        's4': sample_data['nodetags'].get('s4', {}).get('Value'),
        's5': sample_data['nodetags'].get('s5', {}).get('Value'),
        's6': sample_data['nodetags'].get('s6', {}).get('Value'),
        's7': sample_data['nodetags'].get('s7', {}).get('Value'),
        's8': sample_data['nodetags'].get('s8', {}).get('Value'),
        's9': sample_data['nodetags'].get('s9', {}).get('Value'),
        'tmp': sample_data['nodetags'].get('tmp', {}).get('Value'),
        'hum': sample_data['nodetags'].get('hum', {}).get('Value'),
        'pre': sample_data['nodetags'].get('pre', {}).get('Value'),
        'vcc': sample_data['nodetags'].get('vcc', {}).get('Value')
    }

    # Get the 'hum' value
    hum_value = filtered_data['hum']

    # Push the 'hum' value to Resiot, updating the 'smk' value
    resiot_http_push('3a6e00000000aaaa', filtered_data['deveui'], 'smk', hum_value)

if __name__ == "__main__":
    main()
