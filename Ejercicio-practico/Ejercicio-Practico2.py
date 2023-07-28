# Author juan david ramirez grismaldo
# date 23/07/2023

# Ejercicio 2

# A.) pedir la edad de los compañerops que vinieron a clase y ordenar de menor a mayor
# B.) el mayor es el profesor y el menor es el asistente quien es quien
# pedir nombre y edad de estudiantes
def obterner_compañeros(cantidad):
    Compañeros = []
    for i in range(cantidad):
        nombre = input("ingrese nombre: ")
        edad = int(input("ingrese edad: "))
        Compañeros.append([nombre, edad])
    Compañeros.sort(key=lambda x: x[1])
    Profesor = Compañeros[-1]
    Asistente = Compañeros[0]
    return Asistente, Profesor


# ordenar de menor a mayor
asistente, profesor = obterner_compañeros(4)
print(f"el Pofesor es {profesor} y el asistente es {asistente}")

# parte dos del ejercicio
# crear una funcio que devuelva los numero primos desde 0 hasta n


def obtener_numeros_primos(n):
    numeros_primos = []
    for i in range(n):
        if i % 2 != 0:
            numeros_primos.append(i)
    return numeros_primos


print("numeros primos de rango dado")
print(obtener_numeros_primos(13))

# parte 3 del ejercicio
# retornar los numeros primos de la serie de bibonacci


def obtener_fibonacci(n):
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    return fibonacci


print("numeros de la serie de fibonacci")
print(obtener_fibonacci(20))
