import streamlit as st
import requests
import pandas as pd
import time

st.title('IoT Data Dashboard')

# Fetch data from the Flask server
@st.cache_data(ttl=60)
def fetch_data():
    try:
        response = requests.get('http://localhost:5000/data')
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error fetching data: {e}")
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

