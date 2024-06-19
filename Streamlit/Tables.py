import pandas as pd
import requests
from io import StringIO
import streamlit as st

# URL of the raw CSV file on GitHub
url1 = 'https://raw.githubusercontent.com/Eduardo-Cordeiro/Economics_UrbanBeauty/main/Streamlit/data_macrozones.csv'
url2 = 'https://raw.githubusercontent.com/Eduardo-Cordeiro/Economics_UrbanBeauty/main/Streamlit/data_neighbors.csv'
# Download the CSV file
response1 = requests.get(url1)
# Check that the request was successful
response1.raise_for_status()  
# Download the CSV file
response2 = requests.get(url2)
# Check that the request was successful
response2.raise_for_status()  



# Read the CSV content into a DataFrame
csv_content1 = response1.text
macrozones = pd.read_csv(StringIO(csv_content1), delimiter=',')

# Read the CSV content into a DataFrame
csv_content2 = response2.text
neighborhoods = pd.read_csv(StringIO(csv_content1), delimiter=',')


# Display the DataFrame
print(macrozones)
print(neighborhoods)

st.table(macrozones)
st.table(neighborhoods)
