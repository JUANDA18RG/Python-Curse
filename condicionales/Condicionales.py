# Author juan david ramirez grismaldo
# Date: 21/07/2021

# Condicionales
# if, elif, else
# if condicion:
# instrucciones
# elif condicion:
# instrucciones
# else:
# instrucciones

# los condicionales se usan para tomar decisiones en el codigo
print("condicionales if y else")
edad = 18
if edad >= 18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")

# los condicionales if, elif y else se usan para tomar decisiones en el codigo
print("condicionales if, elif y else")
numero = 3
if numero == 1:
    print("numero uno")
elif numero == 2:
    print("numero dos")
elif numero == 3:
    print("numero tres")
elif numero == 4:
    print("numero cuatro")
else:
    print("numero no encontrado")

# condionales dentro de otro condicional

print("condicionales dentro de otro condicional")
edad = 18
numero_identidad = 1006463424
if edad >= 18:
    print("eres mayor de edad", "pero debes validar tu identidad")
    if numero_identidad == 1006463424:
        print("tu identidad es correcta")
    else:
        print("no tienes las credenciales correctas")
else:
    print(numero_identidad, "eres menor de edad")
