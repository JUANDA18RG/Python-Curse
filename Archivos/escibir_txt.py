# Author juan david ramirez grismaldo
# date 24/07/2023

# para escribir un archivo se usa la funcion write()
# esta funcion recibe un parametro: el texto a escribir
# si el archivo no existe, se crea

with open("Archivos\\archivo.txt", 'a', encoding="utf-8") as archivo:
    # agreagar una linea
    archivo.write("hola mundo\n")
    # agregar varias lineas
    archivo.writelines(["jajajajaj\n", "funciona \n", "perro\n"])
