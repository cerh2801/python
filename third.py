def get_guess():
    guess=input('Ingrese la edad que tiene:\n')
    return guess

def main():
    guess= get_guess()
    if guess == 50:
        print('Correcto')
    else:
        print('incorrecta')

main()
