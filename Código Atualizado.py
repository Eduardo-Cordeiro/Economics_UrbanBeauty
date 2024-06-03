import pandas as pd
import numpy as np
from openpyxl import load_workbook

global Nomes, Nomes_cada, Longitude, Latitude, Longs_Parques, Lats_Parques, latskm_centro, longskm_centro, Nomes_MZ

# Abrir pasta xl
data = pd.read_excel("C:\\Users\\eduar\\Desktop\\GitHubProjects\\TCC\\Código Atualizado\\Dados_Vértices.xlsx")

data_parques = pd.read_excel("C:\\Users\\eduar\\Desktop\\GitHubProjects\\TCC\\Código Atualizado\\Locais_Históricos.xlsx")

#Separar x e y para cada bairro
Nomes = data['NOME']
Longitude = data['Long']
Latitude = data['Lat']

#Definindo listas
Nomes_List = []
Longitude_List = []
Latitude_List = []

#Transformar Series em List
for i in Nomes:
    Nomes_List.append(i)
for i in Longitude:
    Longitude_List.append(i)
for i in Latitude:
    Latitude_List.append(i)
#Ordem alfabetica
Nomes_cada = list(set(Nomes))
Nomes_cada.sort()

#função para selecionar latitudes dos vértices
def selectlat_bairro(a):

    name = a
    b = Nomes_List.count(name)
    c = Nomes_List.index(str(name))
    clat = Latitude_List[c:(c+b)]
    return clat
#função para selecionar longitudes dos vértices
def selectlong_bairro(a):

    name = a
    b = Nomes_List.count(name)
    c = Nomes_List.index(str(name))
    clong = Longitude_List[c:(c+b)]
    return clong

##########################################################################


#calculando área do polígono

def area_calc(x,y):
    nx = len(x)
    som = []
    count = -1
    for i in x:
        count = count + 1

        if int(count) == (int(nx) - 1):
            s = (x[count]*y[count-nx+1]) - (x[count-nx+1]*y[count])
            som.append(s)
        elif int(count) < (int(nx) - 1):
            s = (x[count]*y[count+1]) - (x[count+1]*y[count])
            som.append(s)
    A = sum(som)/2
    return A



#calculando x do centroide
def calcx_centroid(x,y):
    count_x = -1
    nx = len(x)
    som_x = []
###
    som = []
    count = -1
    for i in x:
        count = count + 1

        if int(count) == (int(nx) - 1):
            s = (x[count] * y[count - nx + 1]) - (x[count - nx + 1] * y[count])
            som.append(s)
        elif int(count) < (int(nx) - 1):
            s = (x[count] * y[count + 1]) - (x[count + 1] * y[count])
            som.append(s)
    A = sum(som) / 2
###

    for i in x:
        count_x = count_x + 1

        if int(count_x) == (int(nx) - 1):
            c = som[count_x] * (x[count_x]+x[count_x-nx+1])
            som_x.append(c)
        elif int(count_x) < (int(nx) - 1):
            c = som[count_x] * (x[count_x]+x[count_x+1])
            som_x.append(c)
    Cx = (sum(som_x))/(6*A)
    return(Cx)


#calculando y do centroide
def calcy_centroid(x,y):
    count_y = -1
    nx = len(x)
    som_y = []

###
    som = []
    count = -1
    for i in x:
        count = count + 1

        if int(count) == (int(nx) - 1):
            s = (x[count] * y[count - nx + 1]) - (x[count - nx + 1] * y[count])
            som.append(s)
        elif int(count) < (int(nx) - 1):
            s = (x[count] * y[count + 1]) - (x[count + 1] * y[count])
            som.append(s)
    A = sum(som) / 2


###
    for i in y:
        count_y = count_y + 1

        if int(count_y) == (int(nx) - 1):
            d = som[count_y] * (y[count_y]+y[count_y-nx+1])
            som_y.append(d)
        elif int(count_y) < (int(nx) - 1):
            d = som[count_y] * (y[count_y]+y[count_y+1])
            som_y.append(d)
    Cy = (sum(som_y))/(6*A)
    return Cy


centros_x = []
centros_y = []


for i in Nomes_cada:
    long_selected = selectlong_bairro(i)
    lat_selected = selectlat_bairro(i)
    centroid_x = calcx_centroid(lat_selected, long_selected)
    centroid_y = calcy_centroid(lat_selected, long_selected)
    centros_x.append(centroid_x)
    centros_y.append(centroid_y)


# Dados das coordenadas dos parques
nomes_parques = data_parques['Nome']
lat_parques = data_parques['Lat']
long_parques = data_parques['Long']
latskm_parques = []
longskm_parques = []





#calcula a distancia entro dois pontos no plano cartesiano
def dist(x_centro,y_centro,x_parque,y_parque):
    r = 6371
    phi1 = np.radians(y_parque)
    phi2 = np.radians(y_centro)
    delta_phi = np.radians(y_parque - y_centro)
    delta_lambda = np.radians(x_parque - x_centro)
    a = np.sin(delta_phi / 2) ** 2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2) ** 2
    res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
    return np.round(res, 2)

def gravitacional(bairro,longitudes, latitudes):
    index = Nomes_cada.index(str(bairro))
    n = len(long_parques)
    lista_distancias = []
    sqrinv = []
    x = centros_x[index]
    y = centros_y[index]
    for i in range(0,n,1):
        a = dist(x,y,longitudes[i],latitudes[i])
        lista_distancias.append(a)
    for i in lista_distancias:
        b = 1/(i**2)
        sqrinv.append(b)
    c = sum(sqrinv)
    return c

def media(bairro,longitudes, latitudes):
    index = Nomes_cada.index(str(bairro))
    n = len(long_parques)
    lista_distancias = []
    x = centros_x[index]
    y = centros_y[index]
    for i in range(0, n, 1):
        a = dist(x, y, longitudes[i], latitudes[i])
        lista_distancias.append(a)
        b = sum(lista_distancias)/n
    return b


indicegravitacional = []
lenght = len(Nomes_cada)
for i in range(0,lenght,1):
    indice = gravitacional(Nomes_cada[i],long_parques,lat_parques)
    indicegravitacional.append(indice)


print(indicegravitacional)
print(Nomes_cada)
print(len(indicegravitacional))
print(len(Nomes_cada))

#Definir funções VBA
workbook = load_workbook(filename="C:\\Users\\eduar\\Desktop\\GitHubProjects\\TCC\\Código Atualizado\\Indice.xlsx")
spreadsheet = workbook.active

# Inserir valores na tabela xl
#for i in range(0,lenght,1):
#    ii = 'A' + str(i+2)
#    ij = Nomes_cada[i]
#    spreadsheet[ii].value = ij
#    workbook.save(filename="C:/Users/T-Gamer/Desktop/Dados TCC/Indice.xlsx")

for i in range(0,lenght,1):
    ii = 'E' + str(i+2)
    ij = indicegravitacional[i]
    workbook.save(filename="C:\\Users\\eduar\\Desktop\\GitHubProjects\\TCC\\Código Atualizado\\Indice.xlsx")
    spreadsheet[ii].value = ij



