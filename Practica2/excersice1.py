"""Lógica Simple y Cortocircuito"""


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si al menos una de las variables es True.
"""

esta_lloviendo = True
riego_activado = False

piso_mojado = esta_lloviendo or riego_activado

print("Su respuesta es", piso_mojado)

assert piso_mojado