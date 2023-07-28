# Author juan david ramirez grismaldo
# date 21/07/2023

diccionario = {
    "nombre": 'juan',
    "apellido": 'ramirez',
    "edad": 21
}

# La funcion Keys es para obtener las claves del diccionario
claves = diccionario.keys()
print(claves)

# get es para obtener el valor de una clave
valor = diccionario.get("nombre")
print(valor)

# items es para obtener los items del diccionario
items = diccionario.items()
print(items)

# pop es para eliminar un item del diccionario
diccionario.pop("nombre")
print(diccionario)

# popitem es para eliminar el ultimo item del diccionario
diccionario.popitem()
print(diccionario)

# update es para actualizar un item del diccionario
diccionario.update({"nombre": "juan david"})
print(diccionario)

# clear es para limpiar el diccionario
diccionario.clear()
print(diccionario)
