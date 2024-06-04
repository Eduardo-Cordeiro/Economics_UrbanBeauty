import pandas as pd
import numpy as np
from openpyxl import load_workbook

global Nomes, Nomes_cada, Longitude, Latitude, Longs_Parques, Lats_Parques, latskm_centro, longskm_centro, Nomes_MZ

# Abrir pasta xl
data = pd.read_excel("C:\\Users\\eduar\\Desktop\\GitHubProjects\\TCC\\Data\\Dados_Vértices.xlsx")

data_parques = pd.read_excel("C:\\Users\\eduar\\Desktop\\GitHubProjects\\TCC\\Data\\Locais_Históricos.xlsx")

data = data.sort_values(by="NOME")

print(data["NOME"])

bairros = list(set(data["NOME"].to_list()))
bairros.sort()
print(bairros)

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
    count = -1
    for i in x:
        count = count + 1

        ai = (x[count]*y[count+1] + x[-1]*y[0])
        soma.append(ai)
        
        bi = (y[count]*x[count+1] + y[-1]*x[0])
        somb.append(bi)

        return (sum(soma) - sum(somb))*0.5

teste = area_calc(selectcord_bairro(bairros[0],data,"x"),selectcord_bairro(bairros[0],data,"y"))

print(teste)


