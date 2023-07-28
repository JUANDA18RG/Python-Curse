# creando mi propia exepcion personalizada
class miexpcion(Exception):
    def __init__(self, err):
        print(f'el error mas grande de tu vida es: {err}')

# lanzando mi exepcion
# raise miexpcion("mi exepcion")


# capturando mi exepcion
try:
    raise miexpcion("mi exepcion")
except:
    print("error imbecil")
