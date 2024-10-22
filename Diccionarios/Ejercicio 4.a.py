"""Realiza un programa que pida por teclado una serie de asignaturas, con su calificación correspondiente, hasta que introduzca una asignatura en blanco. Posteriormente nos debe mostrar por pantalla la lista de las que están aprobadas (calificación mayor o igual que 5), con su correspondiente nota y la media aritmética de todas las calificaciones (se incluirán también las notas suspensas en la media)"""

# Declaración de variables

from os import system 

# Declaracion de variables:

asignatura = " " # contendrá el nombre de la asignatura (tipo cadena).
calificacion = 0 # nota de la asignatura (tipo float)-
dicAsignatura = {} # Lista con [Nombre de asignatura, calificación].
sumaCalificaciones = 0 #Suma de las notas para hacer, al final, la media aritmetica.

# Programa principal

system("cls")

while(asignatura != ""):
    asignatura = input("intruduce el nombre de la asignatura (ENTER PARA FINALIZAR)")
    if asignatura != "":
        calificacion = float(input("Teclea su calificacion:"))
        dicAsignatura[asignatura] = calificacion
    print("") # Hago un salto de  linea.

for asignatura, calificacion in dicAsignatura.items():
    if calificacion >= 5:
        print(f"La asignatura {asignatura} esta aprobada con un {calificacion}.")
    sumaCalificaciones = sumaCalificaciones + calificacion 

print(f"La media aritmetica de las calificaciones es {sumaCalificaciones/len(dicAsignatura)}")


