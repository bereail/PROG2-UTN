"""
Armar una lista que contenga el primer y el último elemento de la siguiente lista
Restricción: Utilizar el método append junto al indexado simple
"""

lista = ["ho", 3.1416, 42, 81, 6, "la"]
lista_primero_y_ultimo= []

principio=lista[0] 
fin = lista[-1]

lista_primero_y_ultimo.append(principio)
lista_primero_y_ultimo.append(fin)
print (lista_primero_y_ultimo)

assert lista_primero_y_ultimo == ["ho", "la"]


