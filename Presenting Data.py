import pandas as pd
import streamlit as st
import numpy as np
import folium
#Presenting data

neighborhoods = pd.read_csv("C:\\Users\\escordeiro\\Downloads\\Data\\Data\\data_neighbors.csv")
macrozones = pd.read_csv("C:\\Users\\escordeiro\\Downloads\\Data\\Data\\data_macrozones.csv")

#Pining center with Folium
m = folium.Map(location=(-30, -51))

Macrozones_Group = folium.FeatureGroup(name='Macrozones')
Neighborhoods_Group = folium.FeatureGroup(name='Neighborhoods')

small_cities = folium.FeatureGroup(name='Small Cities')

for i in macrozones["MACROZONE"]:
    a = folium.CircleMarker(
        location = (macrozones.loc[macrozones["MACROZONE"] == i,"LAT_CENTER"].values[0], macrozones.loc[macrozones["MACROZONE"] == i,"LONG_CENTER"].values[0]),
        popup = i,
        radius = (macrozones.loc[macrozones["MACROZONE"] == i,'HGI_GEOM_CENTER'].values[0]/100),
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.6,
        )
    a.add_to(Macrozones_Group)

for i in neighborhoods["NEIGHBORHOOD"]:
    b = folium.CircleMarker(
        location = (neighborhoods.loc[neighborhoods["NEIGHBORHOOD"] == i,"LAT_CENTER"].values[0], neighborhoods.loc[neighborhoods["NEIGHBORHOOD"] == i,"LONG_CENTER"].values[0]),
        popup = i,
        radius = (neighborhoods.loc[neighborhoods["NEIGHBORHOOD"] == i,'HGI_GEOM_CENTER'].values[0]/100),
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.6,
        )
    b.add_to(Neighborhoods_Group)

Macrozones_Group.add_to(m)
Neighborhoods_Group.add_to(m)
folium.LayerControl().add_to(m)
m.save("index.html")
