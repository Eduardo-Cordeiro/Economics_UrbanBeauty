import pandas as pd
import numpy as np


# Open xl file
data_neigh = pd.read_excel("C:\\Users\\escordeiro\\Downloads\\Data\\Data\\Neighborhood_Vertices.xlsx")
data_macro = pd.read_excel("C:\\Users\\escordeiro\\Downloads\\Data\\Data\\Macro_Convert_Vertex.xlsx")
data_hist = pd.read_excel("C:\\Users\\escordeiro\\Downloads\\Data\\Data\\Historical_Sites.xlsx")
data_parks = pd.read_excel("C:\\Users\\escordeiro\\Downloads\\Data\\Data\\Parks.xlsx")


data_neigh = data_neigh.sort_values(by="Name")
neighborhoods = list(set(data_neigh["Name"].to_list()))
neighborhoods.sort()

data_macro = data_macro.sort_values(by="Name")
Macrozones = list(set(data_macro["Name"].to_list()))
Macrozones.sort()

# Select all latitude or longitude coordinates of a specific subdivison
def selectcord_neighborhood(neighborhood,df,cord):
    df_filtered = df[df["Name"] == neighborhood]
    A = df_filtered.sort_values(by="INDEX")
    if cord == "x":
        return A["Long"].tolist()
    elif cord == "y":
        return A["Lat"].tolist()

# Calculates the area of a subdivision
def area_calc(x,y):
    nx = len(x)
    soma = []
    count = -1
    for i in x:
        count += 1
        if int(count) == (int(nx) - 1):
            s = (x[count]*y[count-nx+1]) - (x[count-nx+1]*y[count])
            soma.append(s)
        elif int(count) < (int(nx) - 1):
            s = (x[count]*y[count+1]) - (x[count+1]*y[count])
            soma.append(s)
    return sum(soma)/2   

# Calculates the center of a subdivision    
def calc_center(x,y,cord):
    nx = len(x)
    soma = []
    count = -1
    for i in x:
        count = count + 1

        if int(count) == (int(nx) - 1):
            s = (x[count]*y[count-nx+1]) - (x[count-nx+1]*y[count])
            soma.append(s)
        elif int(count) < (int(nx) - 1):
            s = (x[count]*y[count+1]) - (x[count+1]*y[count])
            soma.append(s)
    a = sum(soma)*0.5
    
    count_x = -1
    som_x = []
    count_y = -1
    som_y = []

    if cord == 'x':
        for i in x:
            count_x = count_x + 1

            if int(count_x) == (int(nx) - 1):
                c = soma[count_x] * (x[count_x]+x[count_x-nx+1])
                som_x.append(c)
            elif int(count_x) < (int(nx) - 1):
                c = soma[count_x] * (x[count_x]+x[count_x+1])
                som_x.append(c)
        Cx = (sum(som_x))/(6*a)
        return(Cx)
    
    elif cord == 'y':
        for i in y:
            count_y = count_y + 1

            if int(count_y) == (int(nx) - 1):
                d = soma[count_y] * (y[count_y]+y[count_y-nx+1])
                som_y.append(d)
            elif int(count_y) < (int(nx) - 1):
                d = soma[count_y] * (y[count_y]+y[count_y+1])
                som_y.append(d)
        Cy = (sum(som_y))/(6*a)
        return Cy    

# Distance beetween tow points
def dist(x1,y1,x2,y2):
    r = 6371
    phi1 = np.radians(y2)
    phi2 = np.radians(y1)
    delta_phi = np.radians(y2 - y1)
    delta_lambda = np.radians(x2 - x1)
    a = np.sin(delta_phi / 2) ** 2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2) ** 2
    res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
    return np.round(res, 2)        

# Gravitacional index
def gravit(bairro,neighborhoods,data_center,data_park):
    index = neighborhoods.index(str(bairro))
    lista_dists = []
    sqrinv = []
    x = data_center["LONG_CENTER"][index]
    y = data_center["LAT_CENTER"][index]
    for i in range(0,len(data_park["Long"]),1):
        a = dist(x,y,data_park["Long"].tolist()[i],data_park["Lat"].tolist()[i])
        lista_dists.append(a)
    for i in lista_dists:
        b = 1/(i**2)
        sqrinv.append(b)
    return sum(sqrinv)

# Average distance of a center in relationsship to all parks of the city
def media(neighborhood,neighborhoods,data_center,data_park):
    index = neighborhoods.index(str(neighborhood))
    n = len(data_park["Long"])

    lista_dists = []
    sqrinv = []
    x = data_center["LAT_CENTRO"][index]
    y = data_center["LONG_CENTRO"][index]
    
    for i in range(0,n,1):
        a = dist(x,y,data_park["Long"].tolist()[i],data_park["Lat"].tolist()[i])
        lista_dists.append(a)
    return sum(lista_dists)/n


#Defining the area and geometrical center of neighborhoods and macrozones
area_neighborhood = []
long_center_neighborhood = []
lat_center_neighborhood = []

for i in neighborhoods:
    area_neighborhood.append(area_calc(selectcord_neighborhood(i,data_neigh,"x"),selectcord_neighborhood(i,data_neigh,"y")))
    long_center_neighborhood.append(calc_center(selectcord_neighborhood(i,data_neigh,"x"),selectcord_neighborhood(i,data_neigh,"y"),'x'))
    lat_center_neighborhood.append(calc_center(selectcord_neighborhood(i,data_neigh,"x"),selectcord_neighborhood(i,data_neigh,"y"),'y'))

area_macrozone = []
long_center = []
lat_center = []

for i in Macrozones:
    area_macrozone.append(area_calc(selectcord_neighborhood(i,data_macro,"x"),selectcord_neighborhood(i,data_macro,"y")))
    long_center.append(calc_center(selectcord_neighborhood(i,data_macro,"x"),selectcord_neighborhood(i,data_macro,"y"),'x'))
    lat_center.append(calc_center(selectcord_neighborhood(i,data_macro,"x"),selectcord_neighborhood(i,data_macro,"y"),'y'))


# creating the dataframes 
data_neighbors = pd.DataFrame()
data_neighbors["NEIGHBORHOOD"] = neighborhoods
data_neighbors["AREA"] = area_neighborhood
data_neighbors["AREA"] = data_neighbors["AREA"].apply(lambda x: abs(x) if x < 0 else x)
data_neighbors["LAT_CENTER"] = lat_center_neighborhood
data_neighbors["LONG_CENTER"] = long_center_neighborhood

data_macrozones = pd.DataFrame()
data_macrozones["MACROZONE"] = Macrozones
data_macrozones["AREA"] = area_macrozone
data_macrozones["AREA"] = data_macrozones["AREA"].apply(lambda x: abs(x) if x < 0 else x)
data_macrozones["LAT_CENTER"] = lat_center
data_macrozones["LONG_CENTER"] = long_center

# defining GI's and its variations

#Neighborhoods 

gi_hist_geom = []
lenght = len(neighborhoods)
for i in range(0,lenght,1):
    index = gravit(neighborhoods[i],neighborhoods,data_neighbors,data_hist)
    gi_hist_geom.append(index)

gi_rec_geom = []
lenght = len(neighborhoods)
for i in range(0,lenght,1):
    index = gravit(neighborhoods[i],neighborhoods,data_neighbors,data_parks)
    gi_rec_geom.append(index)

data_neighbors["HGI_GEOM_CENTER"] = gi_hist_geom
data_neighbors["HRI_GEOM_CENTER"] = gi_rec_geom

#Macrozones

gi_hist_geom = []
lenght = len(Macrozones)
for i in range(0,lenght,1):
    index_macro_geom = gravit(Macrozones[i],Macrozones,data_macrozones,data_hist)
    gi_hist_geom.append(index_macro_geom)

gi_rec_geom = []
lenght = len(Macrozones)
for i in range(0,lenght,1):
    index_macro_geom = gravit(Macrozones[i],Macrozones,data_macrozones,data_parks)
    gi_rec_geom.append(index_macro_geom)

data_macrozones["HGI_GEOM_CENTER"] = gi_hist_geom
data_macrozones["HRI_GEOM_CENTER"] = gi_rec_geom

print(data_neighbors)
print(data_macrozones)



    



















    


















    












