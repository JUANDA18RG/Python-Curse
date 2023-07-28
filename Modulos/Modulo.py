# Author juan david ramirez grismaldo
# Date 24/07/2023

# un modulo es un archivo que contiene una coleccion de funciones que puedes incluir en un script, para utilizarlas en este
# para importar un modulo se utiliza la palabra reservada import seguida del nombre del modulo
# para utilizar una funcion de un modulo se utiliza el nombre del modulo seguido de un punto y el nombre de la funcion.
# ejemplo: import Modulo

# los modulos pueden ser creados por el programador o pueden ser descargados de internet
# para crear un modulo se crea un archivo con extension .py y se guarda en la carpeta del proyecto
# para descargar un modulo se utiliza el comando pip install nombre del modulo

# Ejemplo de modulo creado por el programador
import camelcase as cc
import ModuloSaludar as saludo
import ModuloSaludar as despedida
# para tambien llamar una funcion en especifico se utiliza from nombre del modulo import nombre de la funcion
from ModuloSaludar import saludar, saludar_raro


respuesta = saludo.saludar("Juan David")
print(respuesta)

respuesta2 = despedida.despedir("Juan David")
print(respuesta2)

respuesta3 = saludar("con from")
print(respuesta3)

respuesta4 = saludar_raro("Juan David")
print(respuesta4)
# la carperta de _pycache_ es una carpeta que se crea automaticamente cuando se importa un modulo

# Ejemplo de modulo descargado de internet
# usar el metodo camelcase
# camelcase es para escribir en camelcase
c = cc.CamelCase()
txt = "hola mundo"
print(c.hump(txt))

# propiedades de un modulo
print(dir(saludo))
# para saber el nombre del modulo
print(saludo.__name__)
# para saber el nombre de este modulo
print(__name__)

# para saber la documentacion de un modulo
print(saludo.__doc__)
