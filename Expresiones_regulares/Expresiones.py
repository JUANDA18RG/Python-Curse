# Author juan david ramires grismaldo
# Date 25/07/2023

# las expresiones regulares son una secuencia de caracteres que forma un patron de busqueda

import re

texto = '''hola mi nombre es juan david ramires grismaldo y mi correo es
jajaj ya no te lo voy a dar 21/07/2023  a-029190_2
por pendejo linea 8'''
resultado2 = re.search('mi', texto)
resultado = re.findall('mi', texto)
resultado3 = re.split(' ', texto)
print(resultado)
print(resultado2)
print(resultado3)

# \d-> encuentra digitos
resultado4 = re.findall(r'\d', texto)
print(resultado4)

# \D-> encuentra no digitos
resultado5 = re.findall(r'\D', texto)
print(resultado5)

# \w-> encuentra caracteres alfanumericos
resultado6 = re.findall(r'\w', texto)
print(resultado6)

# \W-> encuentra caracteres no alfanumericos
resultado7 = re.findall(r'\W', texto)
print(resultado7)

# \s-> encuentra espacios en blanco
resultado8 = re.findall(r'\s', texto)
print(resultado8)


# \S-> encuentra caracteres no espacios en blanco
resultado9 = re.findall(r'\S', texto)
print(resultado9)

# ^-> encuentra caracteres al inicio de una cadena
resultado10 = re.findall(r'^hola', texto)
print(resultado10)

# $-> encuentra caracteres al final de una cadena
resultado11 = re.findall(r'8$', texto)
print(resultado11)

# *-> encuentra caracteres que se repiten 0 o mas veces
resultado12 = re.findall(r'p', texto)
print(resultado12)
