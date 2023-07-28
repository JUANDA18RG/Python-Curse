# Author juan david ramirez grismaldo
# date 25/07/2023

# Csv es para leer archivos de texto plano
import csv
# se abre el archivo de texto
with open('Archivos-CSV\\texto.csv',) as File:
    # se lee el archivo de texto
    reader = csv.reader(File)
    # se imprime el archivo de texto
    for row in reader:
        print(row)

# usar libreria pandas para leer archivos de texto plano
import pandas as pd
# se lee el archivo de texto
df = pd.read_csv('Archivos-CSV\\texto.csv')
# se imprime el archivo de texto
print(df)

# para mostrar solo una columna
print(df['nombre'])

# para mostrar solo una fila
print(df.loc[0])
# parta cargarlos de otra forma
df = pd.read_csv('Archivos-CSV\\texto.csv', names=['name', 'lastname', 'age'])
df2 = pd.read_csv('Archivos-CSV\\texto.csv', names=['name', 'lastname', 'age'])
nombres = df.name.tolist()
print(df)

# un slice de un dataframe
cadena = "0123456789"
# el slice es [inicio:fin] el fin no se incluye
print(cadena[2:7])
# con ascending se ordena de forma ascendente si es false es descendente
df_ordenado = df.sort_values(by=['age'], ascending=True)
print(df_ordenado)
# concaternar dos dataframes
df_concatenado = pd.concat([df, df2])
print(df_concatenado)
# funcion haed muestra los primeros registros
primeros_registros = df.head(2)
print(primeros_registros)
# funciuon tail muestra los ultimos registros
ultimos_registros = df.tail(2)
print(ultimos_registros)
# accdiendo  a la cantidad de filas y comlumnas
filas_totales, columnas_totales = df.shape
print(filas_totales, columnas_totales)
# obteniendo data estadistica del dataframe
df_info = df.describe()
print(df_info)

# accdiendo a un elemento especifico con  loc
elemento = df.loc[:, 'lastname']
print(elemento)

# accediendo a un elemento especifico con iloc
elementow = df.iloc[3, :2]
print(elementow)

# accediendo a todos los elementos de las filas de una colmna
apellido = df.loc[2, :]
print(apellido)
