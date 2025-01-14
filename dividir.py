def suma(a,b):
    return a+b

def numeros(suma):
    a = int(input('Ingresa el primer número\n'))
    b = int(input('Ingresar el segundo número\n'))
    result = suma(a,b)
    print(result)
    return suma
    

numeros(suma)