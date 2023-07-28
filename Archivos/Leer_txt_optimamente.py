# Author juan david ramirez grismaldo
# date 24/07/2023

# la mejor manera de leer un archivo es con un ciclo for
# esto es porque no se necesita cerrar el archivo
# y porque se lee linea por linea

# leer el archivo con with
with open("Archivos\\archivo.txt", encoding="utf-8") as archivo:
    print(archivo.read())
# no es necesario cerrar el archivo con with
