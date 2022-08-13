"""
Armar una lista que contenga el primer y el último elemento de la siguiente lista
Restricción: Utilizar el método append junto al indexado simple
"""

lista = ["ho", 3.1416, 42, 81, 6, "la"]
lista_primero_y_ultimo = []
primero = lista.pop(0)
ultimo = lista.pop(-1)

lista_primero_y_ultimo = primero + ultimo

print(lista_primero_y_ultimo)

assert lista_primero_y_ultimo == ["ho", "la"]