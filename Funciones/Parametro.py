# forma optima de pasar parametros

# se utiliza el asterisco para pasar parametros
def mi_funcion(*numeros):
    for numero in numeros:
        print(numero)


resultado = mi_funcion(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# se utiliza el asterisco para pasar parametros


def suma(nombre, *numeros):
    return f"la suma de {nombre} es {sum(numeros)}"


resultado = suma("juan", 5, 6, 7, 8, 9, 10)
print(resultado)

# forma no optima de pasar parametros


def mi_funcion(*args):
    print(args)
    return sum(args)


resultado2 = mi_funcion(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"la suma es {resultado2}")
