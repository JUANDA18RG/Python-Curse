# Author juan david ramirez grismaldo
# date 23/07/2023

# creando un diccionario con dict
diccionario = dict(nombre="juan david", apellido="ramirez", edad=21)
print("creando un diccionario con dict")
print(diccionario)

# las listas no pueden ser claves de un diccionario
# las tuplas si pueden ser claves de un diccionario
# los diccionarios no pueden ser claves de un diccionario
# los conjuntos no pueden ser claves de un diccionario

# creando dioccionarios con fromkeys
# fromkeys crea un diccionario con las claves que se le pasen y con un valor por defecto que se le pase tambien
diccionario = dict.fromkeys(["a", "b", "c", "d"], "valor por defecto")
print("creando dioccionarios con fromkeys")
print(diccionario)
