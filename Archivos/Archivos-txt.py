# Author juan david ramirez grismaldo
# date 24/07/2023

# el manejo de archivos en python es muy sencillo
# para abrir un archivo se usa la funcion open()
# esta funcion recibe dos parametros: el nombre del archivo y el modo de apertura
# los modos de apertura son:
# r: lectura
# w: escritura
# a: agregar
# x: crear
# t: texto
# b: binario
# el modo de apertura es opcional, por defecto es r
# si se abre un archivo en modo escritura y este no existe, se crea
# si se abre un archivo en modo escritura y este existe, se sobreescribe
# si se abre un archivo en modo lectura y este no existe, se genera un error

archivo = open("Archivos\\archivo.txt", encoding="utf-8")
# leer el archivo
print("leer el archivo")
# print(archivo_sin_leer.read())
# leer una linea
print("leer una linea")
Linea = archivo.readline()
# print(Linea)
# ler todas las lineas
print("leer todas las lineas")
print(archivo.readlines())
# cerrar el archivo
archivo.close()
