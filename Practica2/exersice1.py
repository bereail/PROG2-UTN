def maximo_basico(a: float, b: float) -> float:
    """Toma dos números y devuelve el mayor."""
    

print("Ingrese el primer numero: ")
a = float(input())
print("Ingrese el segundo numero: ")
b = float(input())


if a > b:
    print("El numero",a,"es mayor que",b)
elif b > a:
    print("El numero",b,"es mayo que",a)
else:
    print("Ambos numeros son iguales")