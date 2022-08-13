"""Strings"""


"""
Formatear las siguientes variables de tipo string en un único string.
Restricción: Utilizar el operador +.
"""

variable_01 = "¡Buenos "
variable_02 = "días "
variable_03 = "a todos!"

strings_concatenados = str(variable_01) + str(variable_02) + str(variable_03)

print(strings_concatenados)


assert strings_concatenados == "¡Buenos días a todos!"