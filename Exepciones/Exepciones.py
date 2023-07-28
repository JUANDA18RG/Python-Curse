# Author juan david ramires grimsldo
# Date 25/07/2023

# las exepciones son errores que se presentan en tiempo de ejecucion
# y detienen el programa

# exepciones comunes
# ZeroDivisionError
# NameError
# TypeError
# ValueError
# IndexError
# KeyError
# FileNotFoundError

# ejemplo de exepcion
def sumar():
    # inicio un ciclo infinito
    while True:
        a = input("ingrese un numero: ")
        b = input("ingrese otro numero: ")
        # intento convertir los numeros a enteros
        try:
            resultado = int(a)+int(b)
        # si no se puede por que no son numeros
        except Exception as e:
            print("error al sumar no es un numero idiota")
            print(f'error: {e}')
        # continuo el ciclo
        else:
            # si se puede sumar salgo del ciclo
            break
        finally:
            # se ejecuta siempre al final del ciclo
            print("se ejecuta siempre")
     # retorno el resultado
    return resultado


print(sumar())
