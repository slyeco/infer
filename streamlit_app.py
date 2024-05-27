# streamlit_app.py
import streamlit as st
import requests

st.title('Treeage Dashboard')

# Fetch data from the Flask server
def fetch_data():
    response = requests.get('http://localhost:5000/data')
    if response.status_code == 200:
        return response.json()
    else:
        return []

st.subheader('Received JSON Data')
data = fetch_data()

# Display the received JSON data
for idx, item in enumerate(data):
    st.write(f"Data {idx+1}: {item}")

st.subheader('Send JSON Data')
input_data = st.text_area('Enter JSON data to send')

if st.button('Send'):
    try:
        json_data = json.loads(input_data)
        response = requests.post('http://localhost:5000/receive', json=json_data)
        if response.status_code == 200:
            st.success('Data sent successfully')
        else:
            st.error('Failed to send data')
    except json.JSONDecodeError:
        st.error('Invalid JSON data')
