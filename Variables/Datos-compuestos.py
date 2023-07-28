# Author juan david ramirez grismaldo
# date 21/07/2023


# los datos compuestos son aquellos que permiten almacenar varios valores
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [1, "juan", 1.75, True]

# imprimir una lista
print(lista)
print(lista2)

# para llamar un elemento de la lista se hace con el nombre de la lista y la posicion del elemento
print(lista[0])
print(lista2[1])

# para cambiar el valor de un elemento de la lista se hace con el nombre de la lista y la posicion del elemento
lista[0] = 100
print(lista)

# las tuplas son listas que no se pueden modificar
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tupla2 = (1, "juan", 1.75, True)

# imprimir una tupla
print(tupla)
print(tupla2)

# para llamar un elemento de la tupla se hace con el nombre de la tupla y la posicion del elemento
print(tupla[0])
print(tupla2[1])

# el conjunto set es una coleccion de datos sin indice y sin orden y no muestra datos repetidos
conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
conjunto2 = {1, "juan", 1.75, True}

# imprimir un conjunto
print(conjunto)
print(conjunto2)

# para llamar un elemento del conjunto se hace con el nombre del conjunto y el elemento
print(1 in conjunto)
print("juan" in conjunto2)

# el diccionario es una coleccion de datos que se almacenan con un indice, pero este indice puede ser una cadena
diccionario = {
    "nombre": "juan",
    "apellido": "ramirez",
    "edad": 18,
    "estatura": 1.75,
    "soltero": True
}

# imprimir un diccionario
print(diccionario)

# para llamar un elemento del diccionario se hace con el nombre del diccionario y el indice
print(diccionario["nombre"])
print(diccionario["soltero"])
