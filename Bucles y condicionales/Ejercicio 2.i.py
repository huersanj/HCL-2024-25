"""Pida por teclado números, hasta que introduzca el 0. Posteriormente debe mostrar su suma y su producto."""

# Declaracion de variables.

numero = 1 # Valor numerrico que voy a pedir por teclado.
suma = 0 # Contendra la suma de todos los valores metidos por teclado.
producto = 1 # Debe almmacenar la multiplicación de todos los numeros.

# Programa principal:

while numero != 0:
    suma = suma + numero 
    producto = producto * numero 
    numero = float(input("introduce el nummero, por favor: "))

print(f"La suma es {suma-1} y la multiplicacion es {producto} ")
