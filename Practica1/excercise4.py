"""
Calcular la cantidad de unidades a comprar.
Restricción: Usar el operador de división entera.
"""

precio = 3.74
presupuesto_disponible = 10

cantidad_a_comprar = presupuesto_disponible // precio

print("La canidad a comprar es de: ", cantidad_a_comprar)

assert cantidad_a_comprar == 2

