"""(Estructura “elif”) Pide por teclado un valor entre 0 y 7 y debe indicarnos por pantalla el día de la semana correspondiente."""

# Declaracion de variables:

diaSemana = 0 # contiene el valor numerico del orden del dia de la semana
nombresDias = ("Lunes", "Martes", "Miercoles","Jueves","Viernes","Sabado","Domingo")

# Porogramada principal:

diaSemana = int(input("Teclea el numero del dia de la semana (1-7): "))
print(f"el dia de la semana es {nombresDias[diaSemana-1]}")




