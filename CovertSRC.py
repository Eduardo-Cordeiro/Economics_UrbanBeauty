#Converting SRC from ESPG:3875 to ESPG:4326
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
lats=[]
longs=[]
for i in range(0,len(data["Lat"]),1):
    x_3857, y_3857 = data["Lat"][i], data["Long"][i]
    latitude, longitude = transformer.transform(x_3857, y_3857)
    lats.append(latitude)
    longs.append(longitude)
# Atribute values to DF
data["Lat_Conv"] = lats
data["Long_Conv"] = longs

print(data)

data.to_excel("C:\\Data\\Macro_Convert_Vertex.xlsx")
