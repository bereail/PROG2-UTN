"""
Agregar la variable variable_01 en la tercer posición de la lista lista_nueva
Restricción: Utilizar el método insert
"""

variable_01 = 2
lista_nueva = [0, 1, 3, 4]

lista_nueva.insert(2, variable_01)

print(lista_nueva)

assert lista_nueva == [0, 1, 2, 3, 4]
