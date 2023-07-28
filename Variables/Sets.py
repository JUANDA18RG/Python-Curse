# Author juan david ramires grismaldo
# date 23/07/2023

# creamdo un conjunto con set
conjunto = set(["juan david", ("dato1", "dato2"), 21])
print(conjunto)

# creamdo un diccionario con dict
diccionario = dict(nombre="juan david", apellido="ramirez", edad=21)
print(diccionario)

# crear conjunto con Frozenset
conjunto = frozenset(["juan david", ("dato1", "dato2"), 21])
conjunto2 = frozenset(["dalto", ("Fada", "ganador"), 2023])
conjunto3 = conjunto | conjunto2
print(conjunto3)

# teoria de conjuntos
# union
# interseccion
# diferencia
# diferencia simetrica
# subconjunto

# subconjunto
conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
conjunto2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

resultado = conjunto.issubset(conjunto2)
resultado2 = conjunto2.issubset(conjunto)
# el menor igual es lo mismo que issubset
resultado3 = conjunto <= conjunto2
resultado4 = conjunto2 <= conjunto
print("subconjunto: ")
print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)

# union
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {6, 7, 8, 9, 10}
conjunto3 = conjunto | conjunto2
print("union: ")
print(conjunto3)


# interseccion
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
conjunto3 = conjunto & conjunto2
print("interseccion: ")
print(conjunto3)

# diferencia
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
conjunto3 = conjunto - conjunto2
print("diferencia: ")
print(conjunto3)

# diferencia simetrica
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
conjunto3 = conjunto ^ conjunto2
print("diferencia simetrica: ")
print(conjunto3)
