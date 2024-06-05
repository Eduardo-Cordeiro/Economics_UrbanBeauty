import pandas as pd
import numpy as np
from openpyxl import load_workbook


# Abrir pasta xl
data = pd.read_excel("C:\\Users\\eduar\\Desktop\\GitHubProjects\\TCC\\Data\\Dados_Vértices.xlsx")

data_parques = pd.read_excel("C:\\Users\\eduar\\Desktop\\GitHubProjects\\TCC\\Data\\Locais_Históricos.xlsx")

data = data.sort_values(by="NOME")

bairros = list(set(data["NOME"].to_list()))
bairros.sort()


def selectcord_bairro(bairro,df,cord):

    df_filtered = df[df["NOME"] == bairro]
    if cord == "x":
        return df_filtered["Lat"].tolist()
    elif cord == "y":
        return df_filtered["Long"].tolist()

def area_calc(x,y):
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
    A = sum(soma)/2
    return A   
    
teste = area_calc(selectcord_bairro(bairros[0],data,"x"),selectcord_bairro(bairros[0],data,"y"))
print('#########3')
print(teste)

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
        
lat_centro = []
long_centro = []
for i in bairros:
    lat_centro.append(calc_center(selectcord_bairro(i,data,"x"),selectcord_bairro(i,data,"y"),'x'))
    long_centro.append(calc_center(selectcord_bairro(i,data,"x"),selectcord_bairro(i,data,"y"),'y'))
    
data_tratada = pd.DataFrame()
data_tratada["BAIRROS"] = bairros
data_tratada["LAT_CENTRO"] = lat_centro
data_tratada["LONG_CENTRO"] = long_centro



