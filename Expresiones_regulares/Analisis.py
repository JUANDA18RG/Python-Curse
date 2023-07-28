import re

texto = "En esta cadena se encuentra una palabra mágica"
# para buscar una palabra
x = re.search("^En.*mágica$", texto)
if x:
    print("Hemos encontrado la palabra")
else:
    print("No se ha encontrado la palabra")

# para remplanzar una palabra
texto = "Hola mundo"
new_text = re.sub("mundo", "Juan", texto)
print(new_text)

# para dividir una cadena
texto = "example@gamil.com.co"
# para validar un correo
pattern = "[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]"

resultado = re.match(pattern, texto)

# se hace le try para que no se caiga el programa
if resultado:
    print("Correo valido")
else:
    print("Correo invalido")

# detectando un numero de telefono y oculatandolo
texto = "Mi numero es 555-123-4567"
# para validar un numero de telefono
pattern = "\d{3}-\d{3}-\d{4}"
remplazo = re.sub(pattern, "###-###-####", texto)
print(remplazo)
