import pandas as pd
import requests
from io import StringIO
import streamlit as st
import folium
from streamlit_folium import st_folium
import folium.plugins
import numpy as np


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
neighborhoods = pd.read_csv(StringIO(csv_content2), delimiter=',')

# Display the DataFrame
macrozones.rename(columns={'Unnamed: 0': 'Index'}, inplace=True)
neighborhoods.rename(columns={'Unnamed: 0': 'Index'}, inplace=True)

print(macrozones)
print(neighborhoods)

# Build Dash

st.markdown(f"Macrozones DataFrame")
st.dataframe(macrozones,hide_index=True,use_container_width=True)

st.markdown(f"Neighborhoods DataFrame")
st.dataframe(neighborhoods,hide_index=True,use_container_width=True)




#Genarating Map

def selectcord_neighborhood(neighborhood,df):
    lista = []
    df_filtered = df[df["Name"] == neighborhood]
    A = df_filtered.sort_values(by="INDEX")
    long = A["Long"].tolist()
    lat = A["Lat"].tolist()
    for i in range(0,len(long),1):
        pair = [lat[i],long[i]]
        tup = tuple(pair)
        lista.append(tup)
    return lista

#Loading data
neigh_vertex = pd.read_excel("Neighborhood_Vertices.xlsx")
macro_vertex = pd.read_excel("Macro_Convert_Vertex.xlsx")


neigh_vertex = neigh_vertex.sort_values(by="Name")
neighborhoods_names = list(set(neigh_vertex["Name"].to_list()))
neighborhoods_names.sort()

macro_vertex = macro_vertex.sort_values(by="Name")
macro_names = list(set(macro_vertex["Name"].to_list()))
macro_names.sort()


#Pining center with Folium
m = folium.Map(location=(-30.0225, -51.1010))

polygon = folium.FeatureGroup(name='Polygon Layer')
#Add Polygons
for i in neighborhoods_names:
    print(selectcord_neighborhood(i,neigh_vertex))
    folium.Polygon(
        locations=selectcord_neighborhood(i,neigh_vertex),
        color="purple",
        weight=6,
        fill_color="purple",
        fill_opacity=0.4,
        fill=True,
        popup=i,   
    ).add_to(polygon)

for i in macro_names:
    print(selectcord_neighborhood(i,macro_vertex))
    folium.Polygon(
        locations=selectcord_neighborhood(i,macro_vertex),
        color="purple",
        weight=6,
        fill_color="purple",
        fill_opacity=0.4,
        fill=True,
        popup=i,   
    ).add_to(polygon)

#Groups
Macrozones_Group = folium.FeatureGroup(name='🚩 Macrozones')
Neighborhoods_Group = folium.FeatureGroup(name='🚩 Neighborhoods')
#Macro SubGroups
Macro_Historical = folium.plugins.FeatureGroupSubGroup(Macrozones_Group, ' ➡️ Macro Historic Index')
Macro_Recreacional = folium.plugins.FeatureGroupSubGroup(Macrozones_Group, ' ➡️ Macro Recreacional Index',show=False)
#Inside Macro Historical SubGroups
Macro_Historical_Geom = folium.plugins.FeatureGroupSubGroup(Macro_Historical, '➖  Macrozone Historic Index Geometric Center')
Macro_Historical_Pop = folium.plugins.FeatureGroupSubGroup(Macro_Historical, '➖  Macrozone Historic Index Populational Center',show=False)
#Inside Macro Recreacional SubGroups
Macro_Recreacional_Geom = folium.plugins.FeatureGroupSubGroup(Macro_Recreacional, '➖ Macrozone Recreacional Index Geometric Center',show=False)
Macro_Recreacional_Pop = folium.plugins.FeatureGroupSubGroup(Macro_Recreacional, '➖ Macrozone Recreacional Index Populational Center',show=False)
Macro_Recreacional_Geom_Scored = folium.plugins.FeatureGroupSubGroup(Macro_Recreacional, '➖ Macrozone Scored Recreacional Index Geometric Center',show=False)
Macro_Recreacional_Pop_Scored = folium.plugins.FeatureGroupSubGroup(Macro_Recreacional, '➖ Macrozone Scored Recreacional Index Populational Center',show=False)
#Neighborhood SubGroups
Neighborhood_Historical = folium.plugins.FeatureGroupSubGroup(Neighborhoods_Group, '➡️ Neighborhood Historic Index')
Neighborhood_Recreacional = folium.plugins.FeatureGroupSubGroup(Neighborhoods_Group, '➡️ Neighborhood Recreacional Index',show=False)
#Inside Neighborhood Historical SubGroups
Neighborhood_Historical_Geom = folium.plugins.FeatureGroupSubGroup(Neighborhood_Historical, '➖ Neighborhood Historic Index Geometric Center')
Neighborhood_Historical_Pop = folium.plugins.FeatureGroupSubGroup(Neighborhood_Historical, '➖ Neighborhood Historic Index Populational Center',show=False)
#Inside Neighborhood Recreacional SubGroups
Neighborhood_Recreacional_Geom = folium.plugins.FeatureGroupSubGroup(Neighborhood_Recreacional, '➖ Neighborhood Recreacional Index Geometric Center',show=False)
Neighborhood_Recreacional_Pop = folium.plugins.FeatureGroupSubGroup(Neighborhood_Recreacional, '➖ Neighborhood Recreacional Index Populational Center',show=False)
Neighborhood_Recreacional_Geom_Scored = folium.plugins.FeatureGroupSubGroup(Neighborhood_Recreacional, '➖ Neighborhood Scored Recreacional Index Geometric Center',show=False)
Neighborhood_Recreacional_Pop_Scored = folium.plugins.FeatureGroupSubGroup(Neighborhood_Recreacional, '➖ Neighborhood Scored Recreacional Index Populational Center',show=False)

def MacroSubGroupingGeom(Column):
    for i in macrozones["MACROZONE"]:
        a = folium.CircleMarker(
            location = (macrozones.loc[macrozones["MACROZONE"] == i,"LAT_CENTER"].values[0], macrozones.loc[macrozones["MACROZONE"] == i,"LONG_CENTER"].values[0]),
            tooltip= i,
            popup = round(macrozones.loc[macrozones["MACROZONE"] == i,Column].values[0],3),
            radius = 3*(np.log(macrozones.loc[macrozones["MACROZONE"] == i,Column].values[0]+1)),
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6,
            )
        if Column == 'HGI_GEOM_CENTER':
            a.add_to(Macro_Historical_Geom)
        elif Column == 'RGI_GEOM_CENTER':
            a.add_to(Macro_Recreacional_Geom)
        elif Column == 'RGI_Scored_GEOM_CENTER':
            a.add_to(Macro_Recreacional_Geom_Scored)
    
def MacroSubGroupingPop(Column):
    for i in macrozones["MACROZONE"]:
        a = folium.CircleMarker(
            location = (macrozones.loc[macrozones["MACROZONE"] == i,"LAT_CENTER_POP"].values[0], macrozones.loc[macrozones["MACROZONE"] == i,"LONG_CENTER_POP"].values[0]),
            tooltip= i,
            popup = round(macrozones.loc[macrozones["MACROZONE"] == i,Column].values[0],3),
            radius = 3*(np.log(macrozones.loc[macrozones["MACROZONE"] == i,Column].values[0]+1)),
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6,
            )
        if Column == 'HGI_POP_CENTER':
            a.add_to(Macro_Historical_Pop)
        elif Column == 'RGI_POP_CENTER':
            a.add_to(Macro_Recreacional_Pop)
        elif Column == 'RGI_Scored_POP_CENTER':
            a.add_to(Macro_Recreacional_Pop_Scored)
    
def NeighSubGroupingGeom(Column):
    for i in neighborhoods["NEIGHBORHOOD"]:
        b = folium.CircleMarker(
            location = (neighborhoods.loc[neighborhoods["NEIGHBORHOOD"] == i,"LAT_CENTER"].values[0], neighborhoods.loc[neighborhoods["NEIGHBORHOOD"] == i,"LONG_CENTER"].values[0]),
            tooltip = i,
            popup = round(neighborhoods.loc[neighborhoods["NEIGHBORHOOD"] == i,Column].values[0],3),
            radius = 2*(np.log(neighborhoods.loc[neighborhoods["NEIGHBORHOOD"] == i,Column].values[0]+1)),
            color='red',
            fill=True,
            fill_color='red',
            fill_opacity=0.6,
            )
        if Column == 'HGI_GEOM_CENTER':
            b.add_to(Neighborhood_Historical_Geom)
        elif Column == 'RGI_GEOM_CENTER':
            b.add_to(Neighborhood_Recreacional_Geom)
        elif Column == 'RGI_Scored_GEOM_CENTER':
            b.add_to(Neighborhood_Recreacional_Geom_Scored)

def NeighSubGroupingPop(Column):
    for i in neighborhoods["NEIGHBORHOOD"]:
        b = folium.CircleMarker(
            location = (neighborhoods.loc[neighborhoods["NEIGHBORHOOD"] == i,"LAT_CENTER_POP"].values[0], neighborhoods.loc[neighborhoods["NEIGHBORHOOD"] == i,"LONG_CENTER_POP"].values[0]),
            tooltip= i,
            popup = round(neighborhoods.loc[neighborhoods["NEIGHBORHOOD"] == i,Column].values[0],3),
            radius = 2*(np.log(neighborhoods.loc[neighborhoods["NEIGHBORHOOD"] == i,Column].values[0]+1)),
            color='red',
            fill=True,
            fill_color='red',
            fill_opacity=0.6,
            )
        if Column == 'HGI_POP_CENTER':
            b.add_to(Neighborhood_Historical_Pop)
        elif Column == 'RGI_POP_CENTER':
            b.add_to(Neighborhood_Recreacional_Pop)
        elif Column == 'RGI_Scored_POP_CENTER':
            b.add_to(Neighborhood_Recreacional_Pop_Scored)

columns = list(macrozones.columns[7:])
for i in columns:
    MacroSubGroupingGeom(i)
    MacroSubGroupingPop(i)
    NeighSubGroupingGeom(i)
    NeighSubGroupingPop(i)

polygon.add_to(m)
Macrozones_Group.add_to(m)
Macro_Historical.add_to(m)
Macro_Historical_Geom.add_to(m)
Macro_Historical_Pop.add_to(m)
Macro_Recreacional.add_to(m)
Macro_Recreacional_Geom.add_to(m)
Macro_Recreacional_Pop.add_to(m)
Macro_Recreacional_Geom_Scored.add_to(m)
Macro_Recreacional_Pop_Scored.add_to(m)
Neighborhoods_Group.add_to(m)
Neighborhood_Historical.add_to(m)
Neighborhood_Historical_Geom.add_to(m)
Neighborhood_Historical_Pop.add_to(m)
Neighborhood_Recreacional.add_to(m)
Neighborhood_Recreacional_Geom.add_to(m)
Neighborhood_Recreacional_Pop.add_to(m)
Neighborhood_Recreacional_Geom_Scored.add_to(m)
Neighborhood_Recreacional_Pop_Scored.add_to(m)

folium.LayerControl().add_to(m)

m.save("Map.html")


st.markdown(f"Map")
st_folium(m, width=700, height=500)
