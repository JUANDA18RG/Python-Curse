# Author juan david ramirez grismaldo
# date: 23/07/2023

# Funciones
# Las funciones son un conjunto de instrucciones que realizan una tarea específica y devuelven un resultado.
import random
print("Funciones")


def mi_funcion():
    print("Hola Mundo")


# se hace el llamado de la funcion
mi_funcion()


# Funciones con parametros
# Las funciones pueden recibir parámetros que modifiquen su comportamiento.
print("Funciones con parametros")


def mi_funcion(nombre, sexo):
    sexo.lower()
    if (sexo == "mujer"):
        print("Hola señora", nombre)
    elif (sexo == "hombre"):
        print("Hola señor", nombre)
    else:
        print("Hola lo que seas", nombre)


# se llama la funcion y se le pasa el parametro
mi_funcion("Juan", "hombre")

# crear una funcion que nos devuelve valores


def calculo_contraseña_ramdom(numero):
    chars = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    num_enetero = str(numero)
    num = int(num_enetero[0])
    c1 = num-2
    c2 = num
    c3 = num-5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña, num


# desempaquetado de la funcion
contraseña, num = calculo_contraseña_ramdom(random.randint(0, 100))
print(f"tu contraseña es {contraseña} y tu numero es {num}")
