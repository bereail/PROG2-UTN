"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si la superfice del campo 1 es menor a la del campo 2 y la superficie del
campo 2 es mayor a la del campo 3.
Restricción: Utilizar comparaciones encadenadas - No utilizar and, or ni not.
"""

superficie_de_campo_01 = 85121
superficie_de_campo_02 = 851212
superficie_de_campo_03 = 8512

comparar_superficie = superficie_de_campo_03 < superficie_de_campo_01 > superficie_de_campo_03 < superficie_de_campo_02

print(comparar_superficie)

assert comparar_superficie