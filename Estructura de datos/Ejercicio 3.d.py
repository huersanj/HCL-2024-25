"""Medirá por teclado una palabra y hemos de decir si es un palíndromo o non."""

#Declaración de variables

palabra ="" #Cadena que contenga la palabra a analizar (para ver si es palíndromo)
longitud = 0 #Contendrá el tamaño de la palabra.
indice = 0 # Indice con el que recorremos la palabra.
palindromo = True # Indica si la palabra es palindromo o no.
# Programa principal:


palabra = input("INTRODUCE LA PALABRA PARA VER SI ES PALÍDROMO O NO: ")
longitud = len(palabra) - 1 #Le resto 1 porque la lista formada por la palabra comienza en 0.


while indice < longitud - indice and palindromo == True:
    if palabra[indice] != palabra[longitud - indice]:
        palindromo = False
    indice+=1 

if palindromo == True:
    print(f"La palabra {palabra} es un palíndromo. ")
else: 
    print(f"La palabra {palabra} NO es un palíndromo. ")

