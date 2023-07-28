# Autho: Juan David Ramirez Grismaldo
# Date: 21/07/2021

# Ejercicio practico 1 de curso ded soy dalto sobre Python.

# ejericio 1
# A.) Diferencia en porcentaje entre el curso actual y el reto de cursos.
# B.) Porcentaje de material inservible que se reduce en cada curso.
# C.) ver 10 horas de este curso a cuantas horas de otros cursos equivale.


# variables
minimo = 2.5
promedio = 4
maximo = 7
este_curso = 1.5

# diferencia de duracion en porcentaje
diferencia_minimo = 100 - (este_curso/minimo*100)
print("la diferencia de duracion en porcentaje menos que este curso: ",
      diferencia_minimo)

diferencia_promedio = 100 - (este_curso/promedio*100)
print("la diferencia de duracion en porcentaje menos que este curso: ",
      diferencia_promedio)

diferencia_maximo = 100 - (este_curso/maximo*100)
print("la diferencia de duracion en porcentaje menos que este curso: ",
      diferencia_maximo)

print("------------------------------------------")
# durancio de los tiempos que no sirven
Crudo_promedio = 5
Crudo_curso = 3.5

diferencia_crudo_promedio = 100-promedio/Crudo_promedio*100
print("este curso elimina un porcentaje de duracion de:  ",
      diferencia_crudo_promedio)
diferencia_crudo_curso = 100-este_curso/Crudo_curso*100
print("este curso elimina un porcentaje de duracion de: ",
      diferencia_crudo_curso)

print("------------------------------------------")
# horas de este curso a horas de otros cursos
print("este curso equivale a ", promedio*100 //
      este_curso/10, " horas de otros cursos")

# horas de este curso
print("este curso equivale a ", este_curso*100 //
      promedio/10, " horas de este curso")


# ejercicio 2
# A.) pedirle al usuario que diga cualquier texto real y calcular cuanto tardaria en decir esa frase y cuantas palabras dijo
# B.) si se tarda mas de un 1 minuto en decir la frase, decirle que es muy larga y que la acorte
# C.) Dalto habla un 30% mas rapido cuanto tardaria en decir la frase


texto = input("ingrese un texto: ")

# tiempo de duracion
cantidad_palabras_separadas = texto.split(" ")
cantidad_palabras = len(cantidad_palabras_separadas)

print("dijiste ", {cantidad_palabras}, " palabras",
      " en ", {cantidad_palabras/2}, " segundos")

print("------------------------------------------")
# tiempo de dalto
print("dalto lo diria en ", {cantidad_palabras*100//2*1.3/100}, " segundos")

# Cada palabra se dice en 0.5 segundos
if cantidad_palabras > 120:
    print("es muy largo, acortalo")
