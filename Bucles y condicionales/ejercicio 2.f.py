"""Que lea por teclado 2 números y diga cuál es mayor (considera el caso en que puedan ser iguales)."""

# Declaración de variables

primerNumero = 0
segundoNumero = 0

# Programa principal

primerNumero = float(input("teclee el primer número: "))
segundoNumero = float(input("introduce el segundo número: "))

if primerNumero > segundoNumero: 
    print(f"el primer numero, que es {primerNumero}, es mayor que el segundo numero {segundoNumero}, ")

else:
    if primerNumero == segundoNumero:
        print(f"el primer número, que es {primerNumero}, es IGUAL que el segundo, {segundoNumero}, ")
    else:
        print(f"el primer numero, que es {primerNumero}, es MENOR que el segundo, {segundoNumero}, ")

