"""Pedirá por teclado la lista de los numeros de la loteria de los ultimos 7dias. Posteriormennte los mostrará ordenados de menor a mayor y de mayor a menor"""

# Declaración de variables 

numerosLoteria = [0, 0, 0, 0, 0, 0, 0]

for contador in range(0,7):
    numerosLoteria[contador] = int(input(f"introduce el dia de la loteria del {contador+1}"))

