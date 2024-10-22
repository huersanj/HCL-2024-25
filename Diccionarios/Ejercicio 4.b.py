"""Un programa que lea por teclado una frase y nos devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena."""

# Importacion de libretas.

from os import system 

# Declaracion de variables.

frase =" " # Contiene la cadena de caracteres a escanear.
letra = " " # El carácter que extraemos de la frase (lista)-
dicletras = {} # Diccionario que contendrá: {"letra": nº apariciones}.

# Programa principal: 

system("cls")

frase = input("Teclea la frase a escanear: ")
for letra in frase:
    if letra in dicletras:
        dicletras[letra] += 1
    else:
        dicletras[letra] = 1

for letra,numVeces in dicletras.items():
    if letra != " ":
        print(f"La letra {letra} está {numVeces} en la frase.")
    else:
        print(f"El espacio está {numVeces}. ")

    


