
"""

Construir una expresión lógica que use TODAS 

las variables y cuyo resultado sea

True si el número 1 es divisible por 7 y al mismo

tiempo el número 2 no lo es.
"""


numero_1 = 49

numero_2 = 50

resultado = numero_1 % 7 and numero_2 != numero_2 % 7

print(resultado)

assert resultado

