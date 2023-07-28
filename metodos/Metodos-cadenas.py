# Author Juan David Ramirez Grismaldo
# Date: 21/07/2021

# Metodos de cadenas

# Los metodos de cadenas son funciones que se pueden aplicar a las cadenas

# upper() convierte la cadena a mayusculas
print("upper() convierte la cadena a mayusculas")
cadena = "hola mundo"
print(cadena.upper())

# lower() convierte la cadena a minusculas
print("lower() convierte la cadena a minusculas")
cadena = "HOLA MUNDO"
print(cadena.lower())

# capitalize() convierte la primera letra de la cadena en mayuscula
print("capitalize() convierte la primera letra de la cadena en mayuscula")
cadena = "hola mundo"
print(cadena.capitalize())

# count() cuenta el numero de veces que se repite un caracter en la cadena
print("count() cuenta el numero de veces que se repite un caracter en la cadena")
cadena = "hola mundo"
print(cadena.count("o"))

# find() busca un caracter en la cadena y devuelve su posicion
print("find() busca un caracter en la cadena y devuelve su posicion")
cadena = "hola mundo"
print(cadena.find("m"))

# len() devuelve la longitud de la cadena
print("len() devuelve la longitud de la cadena")
cadena = "hola mundo"
print(len(cadena))

# isdigit() devuelve true si la cadena es un numero
print("isdigit() devuelve true si la cadena es un numero")
cadena = "123"
print(cadena.isdigit())

# isalpha() devuelve true si la cadena es una letra
print("isalpha() devuelve true si la cadena es una letra")
cadena = "hola"
print(cadena.isalpha())

# replace() reemplaza una cadena por otra
print("replace() reemplaza una cadena por otra")
cadena = "hola mundo"
print(cadena.replace("mundo", "juan"))

# split() divide la cadena en una lista
print("split() divide la cadena en una lista")
cadena = "hola,mundo"
print(cadena.split(","))

# strip() elimina los espacios en blanco al inicio y al final de la cadena
print("strip() elimina los espacios en blanco al inicio y al final de la cadena")
cadena = "       hola mundo      "
print(cadena.strip())

# Ejercicio: Solicitar al usuario su nombre y su edad y mostrar en pantalla
# un mensaje con el nombre y la edad del usuario concatenando los datos
# con los metodos de cadenas
print("Ejercicio: Solicitar al usuario su nombre y su edad y mostrar en pantalla")
print("un mensaje con el nombre y la edad del usuario concatenando los datos")
print("con los metodos de cadenas")
nombre = input("ingrese su nombre: ")
edad = input("ingrese su edad: ")
print("su nombre es: " + nombre.capitalize() + " y su edad es: " + edad)


# count es un metodo que cuenta cuantas veces se repite un caracter en una cadena
print("count es un metodo que cuenta cuantas veces se repite un caracter en una cadena")
cadena = "juan david ramirez grismaldo"
print(cadena.count("a"))

# startswith es un metodo que devuelve true si la cadena empieza con el caracter indicado
print("startswith es un metodo que devuelve true si la cadena empieza con el caracter indicado")
cadena = "juan david ramirez grismaldo"
print(cadena.startswith("j"))

# endswith es un metodo que devuelve true si la cadena termina con el caracter indicado
print("endswith es un metodo que devuelve true si la cadena termina con el caracter indicado")
cadena = "juan david ramirez grismaldo"
print(cadena.endswith("o"))

# replace es un metodo que reemplaza una cadena por otra
print("replace es un metodo que reemplaza una cadena por otra")
cadena = "juan david ramirez grismaldo"
print(cadena.replace("david", "daniel"))
