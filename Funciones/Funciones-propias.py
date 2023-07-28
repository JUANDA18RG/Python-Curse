# Author juan david ramirez grismaldo
# Date: 23/07/2023


# encontran el numero mayor de una lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero_mas_alto = max(numeros)
print(numero_mas_alto)

# encontran el numero menor de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)


# redondear un numero
numero_decimal = 3.1416
numero_redondeado = round(numero_decimal, 1)
print(numero_redondeado)


# convertir un numero a binario
numero_binario = bin(10)
print(numero_binario)

# retorna false -> 0, vacio, none,false \ retorna true -> 1, cualquier valor , cadena , datos no vacios.
resultado = bool(1)
print(resultado)

# funvcion all -> retorna true si todos los valores son verdaderos
resultado = all([True, True, True, False])
print(resultado)

# sum
resultado = sum(numeros)
print(resultado)
