"""Que el usuario introduzca un número por teclado y se asegure que está entre 1 y 10 (ambos incluídos). Si no lo es, que vuelva a pedirlo hasta que lo sea. Al final, muéstralo en pantalla."""

# Declaración de variables.

numero = 0

# Porgrama principal.

while numero < 1 or numero > 10:
    numero = int(input("introduce numero por teclado entre 1 y 10: "))

print("El número es:", numero)
