# Author juan david ramirez grismaldo
# date 23/07/2023

# un for en Python es un iterador que recorre una coleccion de datos o un rango de datos

# recorriendo una lista con for
print("recorriendo una lista con for")
lista = ["juan david", "ramirez", 21]
for elemento in lista:
    print("elemento: ", elemento)


# recorriendo una tupla con for
print("recorriendo una tupla con for")
tupla = ("juan david", "ramirez", 21)
for elemento in tupla:
    print("elemento: ", elemento)

# crear lista
animales = ["perro", "gato", "raton", "leon", "tigre"]
numeros = [10, 20, 30, 40, 50]
# recorrer lista animales
print("recorrer lista animales")
for animal in animales:
    print(f'el animal es: {animal}')

# recorrer lista numero
print("recorrer lista numero")
for numero in numeros:
    resultado = numero * 10
    print(f'el numero es: {resultado}')

# recorrer dos listas
print("recorrer dos listas")
for animal, numero in zip(animales, numeros):
    print(f'el animal es: {animal}')
    print(f'el numero es: {numero}')


# recorrer lista animales con range
print("recorrer lista  con range")
for num in range(5, 10):
    print(num)

# recorrer lista numeros con range
numeros2 = [3, 10, 70, 100, 50]
print("recorrer lista numeros con range")
for num in range(len(numeros2)):
    print(numeros2[num])
# forma correcta de recorrer una lista con range
print("forma correcta de recorrer una lista con range")
for num in enumerate(numeros2):
    indice, valor = num
    print(f'el indice es: {indice} y el valor es: {valor}')


# for con else
print("for con else")
for num in range(5):
    print(num)
else:
    print("el for ha terminado")

# for con break
print("for con break")
for num in range(10):
    if num == 5:
        break
    print(num)
else:
    print("el for ha terminado")

# todo lo anterior funciona con tuplas

# iterar conjuntos
print("iterar conjuntos")
conjunto = {"juan david", "ramirez", 21}
for elemento in conjunto:
    print(elemento)

print("conjuntos con range")
for num in range(len(conjunto)):
    print(f'el numero es: {num}')

# iterar diccionarios
print("iterar diccionarios")
diccionario = {"nombre": "juan david", "apellido": "ramirez", "edad": 21}
for elemento in diccionario:
    print(elemento)

print("iterar diccionarios con items")
for llave, valor in diccionario.items():
    print(f'la llave es: {llave} y el valor es: {valor}')


# eviatndo que el for se detenga con continue
print("eviatndo que el for se detenga con continue")
Frutas = ["manzana", "pera", "mango", "piña", "naranja"]
for fruta in Frutas:
    if fruta == "mango":
        continue
    print(fruta)

# recorriendo un string
print("recorriendo un string")
for letra in "juan david":
    print(letra)
