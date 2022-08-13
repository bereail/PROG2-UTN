"""
Determinar si el número de la variable es divisible por 7.
Restricción: Usar el operador módulo.
"""

numero_incalculable = 2 ** 54 - 1

resultado = numero_incalculable % 7 

es_divisible_por_siete = resultado == 0

print(numero_incalculable,es_divisible_por_siete)

assert es_divisible_por_siete