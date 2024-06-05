import pandas as pd
import numpy as np
from openpyxl import load_workbook

global Nomes, Nomes_cada, Longitude, Latitude, Longs_Parques, Lats_Parques, latskm_centro, longskm_centro, Nomes_MZ

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
    somb = []
    count = 0
    for i in x:
        while count < nx-1:
            ai = (x[count]*y[count+1] + x[-1]*y[0])
            soma.append(ai)
            
            bi = (y[count]*x[count+1] + y[-1]*x[0])
            somb.append(bi)
            count += 1
    return (sum(soma) - sum(somb))*0.5

teste = area_calc(selectcord_bairro(bairros[0],data,"x"),selectcord_bairro(bairros[0],data,"y"))

def calc_center(x,y,cord):
    nx = len(x)
    soma = []
    somb = []
    count = 0
    for i in x:
        while count < nx-1:
            ai = (x[count]*y[count+1] + x[-1]*y[0])
            soma.append(ai)
            
            bi = (y[count]*x[count+1] + y[-1]*x[0])
            somb.append(bi)
            count += 1
    a = (sum(soma) - sum(somb))*0.5
    soma = []
    count = 0

    if cord == 'x':
        for i in x: 
            while count < nx-1:
                soma.append((x[count]+x[count+1])*((x[count]*y[count+1]) - (x[count+1]*y[count])))
                count += 1
        return sum(soma)/(6*a)
    elif cord == 'y':
        for i in x:
            while count < nx-1:
                soma.append((y[count]+y[count+1])*((x[count]*y[count+1]) - (x[count+1]*y[count])))
                count += 1
        return sum(soma)/(6*a)
        
lat_centro = []
long_centro = []
for i in bairros:
    lat_centro.append(calc_center(selectcord_bairro(i,data,"x"),selectcord_bairro(i,data,"y"),'x'))
    long_centro.append(calc_center(selectcord_bairro(i,data,"x"),selectcord_bairro(i,data,"y"),'y'))
    
data_tratada = pd.DataFrame()
data_tratada["BAIRROS"] = bairros
data_tratada["LAT_CENTRO"] = lat_centro
data_tratada["LONG_CENTRO"] = long_centro

print(data_tratada)
