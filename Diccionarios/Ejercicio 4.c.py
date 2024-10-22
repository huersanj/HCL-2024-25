"""Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total."""

# Declaración de librerias:

from os import system 

# Declaracion de variables:

nombreArticulo = " " # Contiene el nombre del artículo a comprar (por teclado).
precioArticulo = "" # Precio del artículo (se pide por teclado).
dicArticulo = {} # Diccionario con formato {"nombre de artículo": precio de articulo}
sumaCompra = 0 # Valor total de la suma de la compra.

# Programa principal

system("cls")

while(nombreArticulo != ""):
    nombreArticulo = input("intruduce el nombre del articulo a añadir a la cesta de la compra ( ENTER para finalizar)")
    if nombreArticulo != "":
        precioArticulo = float(input("Teclea su precio: "))
        dicArticulo[nombreArticulo] = precioArticulo
    print("") # Hago un salto de  linea.

for nombreArticulo, precioArticulo in dicArticulo.items():
    print(f"Articulo: {nombreArticulo}, precio: {precioArticulo}")
    sumaCompra += precioArticulo # Equivale a sumaCompra = sumaCompra + precioArticulo

print(f"El importe total de la compra es {sumaCompra}.")
