while True:

    altura = float(input('Digite sua alturaem metros: '))
    sexo = input('Digite seu sexo: [M / F] ')

    if sexo.upper() == 'M':
        peso_ideal_masculino = (72.7 * altura) - 58
        print(f'Seu peso ideal é {peso_ideal_masculino:.2f}KG.')
    elif sexo.upper() == 'F':
        peso_ideal_feminino = (62.1 * altura) - 44.7
        print(f'Seu peso ideal é {peso_ideal_feminino:.2f}KG.')
    else:
        print('Sexo inválido! Por favor digite M ou F.')