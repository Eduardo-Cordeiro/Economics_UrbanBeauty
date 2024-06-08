import pandas as pd
import numpy as np
from openpyxl import load_workbook


# Abrir pasta xl
data = pd.read_excel("C:\\Users\\eduar\\Desktop\\GitHubProjects\\TCC\\Data\\Dados_Vértices.xlsx")
data_hist = pd.read_excel("C:\\Users\\eduar\\Desktop\\GitHubProjects\\TCC\\Data\\Locais_Históricos.xlsx")
data = data.sort_values(by="NOME")
bairros = list(set(data["NOME"].to_list()))
bairros.sort()

def selectcord_bairro(bairro,df,cord):
    df_filtered = df[df["NOME"] == bairro]
    A = df_filtered.sort_values(by="INDEX")
    if cord == "x":
        return A["Long"].tolist()
    elif cord == "y":
        return A["Lat"].tolist()

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

def dist(x1,y1,x2,y2):
    r = 6371
    phi1 = np.radians(y2)
    phi2 = np.radians(y1)
    delta_phi = np.radians(y2 - y1)
    delta_lambda = np.radians(x2 - x1)
    a = np.sin(delta_phi / 2) ** 2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2) ** 2
    res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
    return np.round(res, 2)        

def gravitacional(bairro,bairros,data_centro,data_parque):
    index = bairros.index(str(bairro))
    lista_distancias = []
    sqrinv = []
    x = data_centro["LONG_CENTER"][index]
    y = data_centro["LAT_CENTER"][index]
    for i in range(0,len(data_parque["Long"]),1):
        a = dist(x,y,data_parque["Long"].tolist()[i],data_parque["Lat"].tolist()[i])
        lista_distancias.append(a)
    for i in lista_distancias:
        b = 1/(i**2)
        sqrinv.append(b)
    return sum(sqrinv)

def media(bairro,bairros,data_centro,data_parque):
    index = bairros.index(str(bairro))
    n = len(data_parque["Long"])

    lista_distancias = []
    sqrinv = []
    x = data_centro["LAT_CENTRO"][index]
    y = data_centro["LONG_CENTRO"][index]
    
    for i in range(0,n,1):
        a = dist(x,y,data_parque["Long"].tolist()[i],data_parque["Lat"].tolist()[i])
        lista_distancias.append(a)
    return sum(lista_distancias)/n


area_bairro = []
lat_centro = []
long_centro = []
for i in bairros:
    area_bairro.append(area_calc(selectcord_bairro(i,data,"x"),selectcord_bairro(i,data,"y")))
    lat_centro.append(calc_center(selectcord_bairro(i,data,"x"),selectcord_bairro(i,data,"y"),'y'))
    long_centro.append(calc_center(selectcord_bairro(i,data,"x"),selectcord_bairro(i,data,"y"),'x'))
    
data_neighbors = pd.DataFrame()
data_neighbors["NEIGHBORHOOD"] = bairros
data_neighbors["AREA"] = area_bairro
data_neighbors["LAT_CENTER"] = lat_centro
data_neighbors["LONG_CENTER"] = long_centro

indicegravitacional = []
lenght = len(bairros)
for i in range(0,lenght,1):
    indice = gravitacional(bairros[i],bairros,data_neighbors,data_hist)
    indicegravitacional.append(indice)
    












