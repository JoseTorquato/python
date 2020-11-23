idade_nadador = input('Qual a idade: ')

if idade_nadador.isnumeric():
    idade_nadador = int(idade_nadador)
    if 5 <= idade_nadador <= 7:
        print('Infantil A')
    elif 8 <= idade_nadador <= 11:
        print('Infantil B')
    elif 12 <= idade_nadador <= 13:
        print('Juvenil A')
    elif 14 <= idade_nadador <= 17:
        print('Juvenil B')
    elif idade_nadador > 18:
        print('Adulto')
    else:
        print('Idade menor que a permitida.')
else:
    print('Digite um idade válida.')
