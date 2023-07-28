# Author juan david ramires grismaldo
# date 23/07/2023


# lambda crea funciones anonimas, es decir, funciones sin nombre

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def multipliacar(numero): return numero * 2

# creando funcuion comun que diga si es par o impar


def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


# usando filter con funcion comun
print(list(filter(es_par, numeros)))

# usando filter con funcion lambda
print(list(filter(lambda numero: numero % 2 == 0, numeros)))
