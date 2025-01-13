def suma(a, b):
    """Suma dos números."""
    return a + b

def obtener_valores():
    """Obtiene dos números del usuario y los suma."""
    a = int(input("Ingrese el primer valor: "))
    b = int(input("Ingrese el segundo valor: "))
    resultado = suma(a, b)
    return resultado

# Llamamos a la función para obtener el resultado
resultado_final = obtener_valores()
print("El resultado de la suma es:", resultado_final)