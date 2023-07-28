# Author juan david ramirez
# Date: 21/07/2021


# Operadores de comparacion
print("operadores de comparacion")
# == igual
# != diferente
# < menor que
# > mayor que
# <= menor o igual que
# >= mayor o igual que

numeroA = 10
numeroB = 5

resultado = numeroA == numeroB
print(resultado)

resultado = numeroA != numeroB
print(resultado)

resultado = numeroA < numeroB
print(resultado)

resultado = numeroA > numeroB
print(resultado)

resultado = numeroA <= numeroB
print(resultado)

resultado = numeroA >= numeroB
print(resultado)

# Operadores logicos
print("operadores logicos")
# and y
# or o
# not no

numeroA = 10
numeroB = 5

resultado = numeroA > numeroB and numeroB > 0
print(resultado)


resultado = numeroA > numeroB or numeroB > 0
print(resultado)

resultado = not (numeroA > numeroB)
print(resultado)

# Operadores de identidad
print("operadores de identidad")
# is
# is not

frutas = ["manzana", "pera"]
frutas2 = ["manzana", "pera"]
frutas3 = frutas

resultado = frutas is frutas2
print(resultado)

resultado = frutas is frutas3
print(resultado)

resultado = frutas is not frutas2
print(resultado)

resultado = frutas is not frutas3
print(resultado)

# Operadores de membresia
print("operadores de membresia")
# in
# not in

frutas = ["manzana", "pera"]

resultado = "manzana" in frutas
print(resultado)

resultado = "manzana" not in frutas
print(resultado)
