"""Que sume todos los números pares positivos, partiendo desde 0, hasta que la suma supere el valor de 1000. Posteriormente, debe mostrar en pantalla cuál es el valor de la suma y cuántos números se han sumado."""

#Declaración de variables.

suma = 0 # donde guardo la suma.
numeroPar = 0 # Variable que utilizo para incrementar de 2 en 2.
contador = 0 # Variable que contará en el número de valores que sumo.

while suma <= 1000: 
    contador = contador + 1 
    numeroPar = numeroPar + 2
    suma = suma + numeroPar

print(f"he usado {contador} numeros pares, y el total de la suma es {suma}")
