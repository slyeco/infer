import json
import urllib.request

# Configuration for ResIOT
resiot_base_url = 'http://15.160.194.92:58089'
resiot_token = '3cef9fccfdf0de6a48a679239e1bed0c'
appEUI = '3A6E00000000AAAA'
devEUI = '3A6E00000000A017'

# Headers for ResIOT API
resiot_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": resiot_token
}

# Function to update 'smk' parameter in ResIOT
def update_smk_parameter(appEUI, devEUI, value):
    endpoint = f"{resiot_base_url}/api/application/{appEUI}/nodes/{devEUI}/tag/smk/value"
    payload = json.dumps({"value": str(value)})
    
    req = urllib.request.Request(endpoint, data=payload.encode('utf-8'), headers=resiot_headers, method="PUT")
    
    try:
        # Send the request
        with urllib.request.urlopen(req) as response:
            response_body = response.read().decode()
            print(f"Update for smk was successful. Response: {response_body}")
    except urllib.error.HTTPError as e:
        # Handle HTTP errors
        print(f"Update for smk failed with status code {e.code}. Response: {e.read().decode()}")

# Test script to set the 'smk' value to 90 for devEUI 3A6E00000000A017
if __name__ == '__main__':
    update_smk_parameter(appEUI, devEUI, 0)
