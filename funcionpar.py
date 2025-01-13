def main():
    x = int(input('Cuál es el número?\n:'))
    if par(x):
        print('Par')
    else:
        print('Impar')

def par(n):
    return True if n %2 == 0 else False

main()
