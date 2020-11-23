recebe_numero = input('Digite um número: ')

if recebe_numero.isnumeric():
    recebe_numero = int(recebe_numero)
    if recebe_numero % 2 == 0:
        print(f'{recebe_numero} é Par.')
    else:
        print(f'{recebe_numero} é Impar.')

    if recebe_numero > 0:
        print(f'{recebe_numero} é um número positivo.')
    else:
        print(f'{recebe_numero} é um número negativo.')
else:
    print('Digite um número válido [-10, 10].')