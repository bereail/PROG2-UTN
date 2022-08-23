# NO MODIFICAR - INICIO
from exersice1 import maximo_basico


assert maximo_basico(10, 5) == 10
assert maximo_basico(9, 18) == 18
# NO MODIFICAR - FIN


###############################################################################


#def maximo_libreria(a: float, b: float) -> float:
"""Re-escribir utilizando el built-in max.
Referencia: https://docs.python.org/3/library/functions.html#max
"""


print("Ingrese el primer numero: ")
a = float(input())
print("Ingrese el segundo numero:")
b = float(input())

maximo_libreria = [a,b]

maximo_basico = max(maximo_libreria)


print("El numero mayo es: ", maximo_libreria)