"""Comparación"""

"""
Construir una expresión lógica que use TODAS las variables 
y cuyo resultado sea
True si 2 personas tienen el mismo nombre pero distinta edad.
Aclaración: Se puede utilizar and, or y not.
"""

persona_01 = "Kevin"
edad_01 = 24
persona_02 = "Kevin"
edad_02 = 41

comparar_nombre_y_edad = persona_01 and persona_02

print(comparar_nombre_y_edad)

assert comparar_nombre_y_edad