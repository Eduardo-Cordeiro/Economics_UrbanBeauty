#convertendo SRC de 3875 para 4326
import pyproj
import pandas as pd

# Define the EPSG codes for the coordinate systems
epsg_3857 = pyproj.CRS('EPSG:3857')
epsg_4326 = pyproj.CRS('EPSG:4326')

# Define the transformer object
transformer = pyproj.Transformer.from_crs(epsg_3857, epsg_4326)

# Sample coordinates in EPSG:3857 (e.g., X and Y coordinates in meters)
data = pd.read_excel("C:/Users/eduar/Desktop/VÉRTICES.xlsx")

# Perform the transformation
longs=[]
lats=[]
for i in range(0,len(data["Long"]),1):
    x_3857, y_3857 = data["Long"][i], data["Lat"][i]
    #Don't know why I had to invert latitude and longitude down here, but it works.
    latitude, longitude = transformer.transform(x_3857, y_3857)
    longs.append(longitude)
    lats.append(latitude)
    
# Atribute values to DF
data["Lat_Conv"] = lats
data["Long_Conv"] = longs

data.to_excel("C:\\Data\\Macro_Convert_Vertex.xlsx")
