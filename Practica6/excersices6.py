"""
Armar una lista que contenga los primeros 2 y los últimos 2 elementos de la
siguiente lista
Restricción: Utilizar el método extend junto al indexado múltiple
"""

lista = ["ho", "la", 81, 6, 42, "como", "estas?"]
lista_primeros_y_ultimos = [4]

lista_primeros_y_ultimos[0] = lista.pop(0)
lista_primeros_y_ultimos[1] = lista.pop(-1)


#ultimo = lista.pop(-1)

#lista_primeros_y_ultimos = lista_primero_y_ultimo.extend([])

print(lista_primeros_y_ultimos)

#assert lista_primeros_y_ultimos == ["ho", "la", "como", "estas?"]