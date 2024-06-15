import pandas as pd
import streamlit as st
import numpy as np
import folium
#Presenting data

neighborhoods = pd.read_csv("C:\\Users\\escordeiro\\Downloads\\Data\\Data\\data_neighbors.csv")
macrozones = pd.read_csv("C:\\Users\\escordeiro\\Downloads\\Data\\Data\\data_macrozones.csv")

#Pining center with Folium
m = folium.Map(location=(-30, -51))

for i in macrozones["MACROZONE"]:
    folium.Marker(
        location = (macrozones.loc[macrozones["MACROZONE"] == i,"LAT_CENTER"].values[0], macrozones.loc[macrozones["MACROZONE"] == i,"LONG_CENTER"].values[0]),
        popup = i,
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

for i in neighborhoods["NEIGHBORHOOD"]:
    folium.Marker(
        location = (neighborhoods.loc[neighborhoods["NEIGHBORHOOD"] == i,"LAT_CENTER"].values[0], neighborhoods.loc[neighborhoods["NEIGHBORHOOD"] == i,"LONG_CENTER"].values[0]),
        popup = i,
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(m)

m.save("index.html")
