"""que lea por tecllado 2 nummeros y diga cual es mayor (supondremos que son diferentes)"""

# Declaración de variables.

primerNumero = 0
segundoNumero = 0

# Programa principal:

primerNumero = float(input("teclea al primer número: "))
segundoNumero = float(input("introduce el segundo número"))

if primerNumero > segundoNumero:
    print(f"El primer numero, que es {primerNumero}, es mayor que el segundo, {segundoNumero},")
else: 
    print(f"El primer numero, que es {primerNumero}, es menor que el segundo, {segundoNumero},")

          