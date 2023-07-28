# Author juan david ramirez grismaldo
# date 21/07/2021

# Metodos de listas

# Los metodos de listas son funciones que se pueden aplicar a las listas
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("lista = [1,2,3,4,5,6,7,8,9,10]")

# len devuelve la longitud de la lista
print("len devuelve la longitud de la lista")
print(len(lista))

# append agrega un elemento al final de la lista
print("append agrega un elemento al final de la lista")
lista.append(11)
print(lista)

# insert agrega un elemento en la posicion indicada
print("insert agrega un elemento en la posicion indicada")
lista.insert(2, "se agrego  esto")
print(lista)

# pop elimina el ultimo elemento de la lista
print("pop elimina el ultimo elemento de la lista")
lista.pop()
print(lista)

# remove elimina el elemento indicado de la lista
print("remove elimina el elemento indicado de la lista")
lista.remove(3)
print(lista)

# clear elimina todos los elementos de la lista
print("clear elimina todos los elementos de la lista")
lista.clear()
print(lista)

# sort ordena los elementos de la lista
print("sort ordena los elementos de la lista")
lista = [5, 2, 1, 3, 4]
lista.sort()
print(lista)

# reverse invierte los elementos de la lista
print("reverse invierte los elementos de la lista")
lista.reverse()
print(lista)
