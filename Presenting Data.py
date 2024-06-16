import folium.plugins
import pandas as pd
import streamlit as st
import numpy as np
import folium
global neighborhoods, macrozones
#Presenting data
neighborhoods = pd.read_csv("C:\\Users\\eduar\\Desktop\\GitHubProjects\\TCC\\Data\\Data\\data_neighbors.csv")
macrozones = pd.read_csv("C:\\Users\\eduar\\Desktop\\GitHubProjects\\TCC\\Data\\Data\\data_macrozones.csv")

#Pining center with Folium
m = folium.Map(location=(-30, -51))
#Groups
Macrozones_Group = folium.FeatureGroup(name='Macrozones')
Neighborhoods_Group = folium.FeatureGroup(name='Neighborhoods')
#Macro SubGroups
Macro_Historical = folium.plugins.FeatureGroupSubGroup(Macrozones_Group, 'Macro Historic Index')
Macro_Recreacional = folium.plugins.FeatureGroupSubGroup(Macrozones_Group, 'Macro Recreacional Index')
#Inside Macro Historical SubGroups
Macro_Historical_Geom = folium.plugins.FeatureGroupSubGroup(Macro_Historical, 'Historic Index Geometric Center')
Macro_Historical_Pop = folium.plugins.FeatureGroupSubGroup(Macro_Historical, 'Historic Index Populational Center')
#Inside Macro Recreacional SubGroups
Macro_Recreacional_Geom = folium.plugins.FeatureGroupSubGroup(Macro_Recreacional, 'Recreacional Index Geometric Center')
Macro_Recreacional_Pop = folium.plugins.FeatureGroupSubGroup(Macro_Recreacional, 'Recreacional Index Populational Center')
Macro_Recreacional_Geom_Scored = folium.plugins.FeatureGroupSubGroup(Macro_Recreacional, 'Scored Recreacional Index Geometric Center')
Macro_Recreacional_Pop_Scored = folium.plugins.FeatureGroupSubGroup(Macro_Recreacional, 'Scored Recreacional Index Populational Center')
#Neighborhood SubGroups
Neighborhood_Historical = folium.plugins.FeatureGroupSubGroup(Neighborhoods_Group, 'Neighborhood Historic Index')
Neighborhood_Recreacional = folium.plugins.FeatureGroupSubGroup(Neighborhoods_Group, 'Neighborhood Recreacional Index')
#Inside Neighborhood Historical SubGroups
Neighborhood_Historical_Geom = folium.plugins.FeatureGroupSubGroup(Neighborhood_Historical, 'Historic Index Geometric Center')
Neighborhood_Historical_Pop = folium.plugins.FeatureGroupSubGroup(Neighborhood_Historical, 'Historic Index Populational Center')
#Inside Neighborhood Recreacional SubGroups
Neighborhood_Recreacional_Geom = folium.plugins.FeatureGroupSubGroup(Neighborhood_Recreacional, 'Recreacional Index Geometric Center')
Neighborhood_Recreacional_Pop = folium.plugins.FeatureGroupSubGroup(Neighborhood_Recreacional, 'Recreacional Index Populational Center')
Neighborhood_Recreacional_Geom_Scored = folium.plugins.FeatureGroupSubGroup(Neighborhood_Recreacional, 'Scored Recreacional Index Geometric Center')
Neighborhood_Recreacional_Pop_Scored = folium.plugins.FeatureGroupSubGroup(Neighborhood_Recreacional, 'Scored Recreacional Index Populational Center')



def MacroSubGrouping(Column):
    for i in macrozones["MACROZONE"]:
        a = folium.CircleMarker(
            location = (macrozones.loc[macrozones["MACROZONE"] == i,"LAT_CENTER"].values[0], macrozones.loc[macrozones["MACROZONE"] == i,"LONG_CENTER"].values[0]),
            popup = i,
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
        elif Column == 'HGI_POP_CENTER':
            a.add_to(Macro_Historical_Pop)
        elif Column == 'RGI_POP_CENTER':
            a.add_to(Macro_Recreacional_Pop)
        elif Column == 'RGI_Scored_POP_CENTER':
            a.add_to(Macro_Recreacional_Pop_Scored)
    
def NeighSubGrouping(Column):
    for i in neighborhoods["NEIGHBORHOOD"]:
        b = folium.CircleMarker(
            location = (neighborhoods.loc[neighborhoods["NEIGHBORHOOD"] == i,"LAT_CENTER"].values[0], neighborhoods.loc[neighborhoods["NEIGHBORHOOD"] == i,"LONG_CENTER"].values[0]),
            popup = i,
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
        elif Column == 'HGI_POP_CENTER':
            b.add_to(Neighborhood_Historical_Pop)
        elif Column == 'RGI_POP_CENTER':
            b.add_to(Neighborhood_Recreacional_Pop)
        elif Column == 'RGI_Scored_POP_CENTER':
            b.add_to(Neighborhood_Recreacional_Pop_Scored)

columns = list(macrozones.columns[5:])
for i in columns:
    MacroSubGrouping(i)
    NeighSubGrouping(i)


Macrozones_Group.add_to(m)
Macro_Historical.add_to(m)
Macro_Recreacional.add_to(m)
Macro_Historical_Geom.add_to(m)
Macro_Historical_Pop.add_to(m)
Macro_Recreacional_Geom.add_to(m)
Macro_Recreacional_Pop.add_to(m)
Macro_Recreacional_Geom_Scored.add_to(m)
Macro_Recreacional_Pop_Scored.add_to(m)

Neighborhoods_Group.add_to(m)
Neighborhood_Historical.add_to(m)
Neighborhood_Recreacional.add_to(m)
Neighborhood_Historical_Geom.add_to(m)
Neighborhood_Historical_Pop.add_to(m)
Neighborhood_Recreacional_Geom.add_to(m)
Neighborhood_Recreacional_Pop.add_to(m)
Neighborhood_Recreacional_Geom_Scored.add_to(m)
Neighborhood_Recreacional_Pop_Scored.add_to(m)


folium.LayerControl().add_to(m)
m.save("Column.html")

