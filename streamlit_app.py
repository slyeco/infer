# streamlit_app.py
import streamlit as st
import requests
import pandas as pd
import time

st.title('IoT Data Dashboard')

# Fetch data from the Flask server
def fetch_data():
    response = requests.get('http://localhost:5000/data')
    if response.status_code == 200:
        return response.json()
    else:
        return []

# Main loop to update the dashboard
while True:
    st.subheader('Last 10 Received JSON Messages')
    data = fetch_data()
    
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.write("No data received yet.")

    # Auto-refresh every 10 seconds
    time.sleep(10)
    st.experimental_rerun()
