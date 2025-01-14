def suma(*args):
    return sum(args)

def numeros():
    nums = []
    while True:
        num = input('Ingresa un número (o presiona Enter para finalizar): ')
        if not num:
            break
        nums.append(int(num))
    return suma(*nums)

resultado = numeros()
print(resultado)