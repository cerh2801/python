def main():
    x = int(input('Cuál es el número?\n:'))
    if par(x):
        print('Par')
    else:
        print('Impar')

def par(n):
    if n%2!=0:
        return False
    else:
        return True

main()
