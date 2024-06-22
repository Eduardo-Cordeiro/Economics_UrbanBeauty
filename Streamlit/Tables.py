import pandas as pd
import requests
from io import StringIO
import streamlit as st
import streamlit.components.v1 as components
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def max_min_norm(df, column_name):
    min_val = df[column_name].min()
    max_val = df[column_name].max()
    
    # Apply the max-min normalization formula
    normalized_column = (df[column_name] - min_val) / (max_val - min_val)
    return normalized_column

def log_norm(df, column_name):
    norm = np.log(df[column_name]+1)

    # Apply the max-min normalization formula
    
    return norm

# URL of the raw CSV file on GitHub
url1 = 'https://raw.githubusercontent.com/Eduardo-Cordeiro/Economics_UrbanBeauty/main/Data/data_macrozones.csv'
url2 = 'https://raw.githubusercontent.com/Eduardo-Cordeiro/Economics_UrbanBeauty/main/Data/data_neighbors.csv'
url3 = 'https://raw.githubusercontent.com/Eduardo-Cordeiro/Economics_UrbanBeauty/main/Data/Wages.csv'
url4 = 'https://raw.githubusercontent.com/Eduardo-Cordeiro/Economics_UrbanBeauty/main/Data/School Dropout.csv'
# Download the CSV file
response1 = requests.get(url1)
response2 = requests.get(url2)
response3 = requests.get(url3)
response4 = requests.get(url4)
# Check that the request was successful
response1.raise_for_status()  
response2.raise_for_status()
response2.raise_for_status()  
response4.raise_for_status() 

# Read the CSV content into a DataFrame
csv_content1 = response1.text
macrozones = pd.read_csv(StringIO(csv_content1), delimiter=',')
csv_content2 = response2.text
neighborhoods = pd.read_csv(StringIO(csv_content2), delimiter=',')
csv_content3 = response3.text
wages = pd.read_csv(StringIO(csv_content3), delimiter=',')
csv_content4 = response4.text
dropout = pd.read_csv(StringIO(csv_content4), delimiter=',')

# Display the DataFrame
macrozones.rename(columns={'Unnamed: 0': 'Index'}, inplace=True)
neighborhoods.rename(columns={'Unnamed: 0': 'Index'}, inplace=True)

# Build Dash
st.markdown(f"Macrozones DataFrame")
st.dataframe(macrozones,hide_index=True,use_container_width=True)

st.markdown(f"Neighborhoods DataFrame")
st.dataframe(neighborhoods,hide_index=True,use_container_width=True)


#Genarating Map
st.markdown(f"Map")
with open("Map.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Use streamlit's components.html to display the HTML content
components.html(html_code, height=600)

#Correlation
cor1 = pd.merge(neighborhoods,wages,on='NEIGHBORHOOD')
correlation_frame = pd.merge(cor1,dropout,on='NEIGHBORHOOD')
columns = ["HGI_GEOM_CENTER","RGI_GEOM_CENTER","RGI_Scored_GEOM_CENTER","HGI_POP_CENTER","RGI_POP_CENTER","RGI_Scored_POP_CENTER","Average Wage (MW)","School Dropout (%)"]

#Normalizing data
for i in columns:
    correlation_frame[str(i)] = log_norm(correlation_frame,str(i))

#Correlation
neighborhood_corr = correlation_frame[columns].corr()
print(neighborhood_corr)
st.markdown(f"Correlation Matrix")

fig, ax = plt.subplots()
sns.heatmap(neighborhood_corr, annot=True, ax=ax)
st.write(fig)
