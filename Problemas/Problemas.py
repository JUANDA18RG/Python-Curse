# 2 listas , una con nombres otra con apelledos

nombres = ["juan", "pedro", "maria", "jose", "luis",
           "jorge", "carlos", "daniel", "javier", "julian"]
apellidos = ["ramirez", "grismaldo", "gomez", "perez", "gonzales",
             "rodriguez", "hernandez", "diaz", "torres", "castro"]

# registra est informacion en un txt de forma optima

with open('Problemas\\datos.txt', 'w') as arch:
    arch.writelines("los datos son: \n")
    [arch.writelines(f"nombreas: {n}\napellido: {a}\n--------------\n")
     for n, a in zip(nombres, apellidos)]

# lee la informacion del txt y la imprime en pantalla
with open('Problemas\\datos.txt', 'r') as arch:
    print(arch.read())
