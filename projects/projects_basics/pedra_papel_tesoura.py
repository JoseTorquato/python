'''
Pedra, Papel e tesoura
regra:
    Pedra > Tesoura
    Tesoura > Papel
    Papel > Pedra

'''
import random

while True:
    bot_escolha_random = ['Pedra', 'Papel', 'Tesoura']

    escolha_usuario = input(f'Escolha uma opção abaixo\n'
                            f'1 - Pedra\n'
                            f'2 - Papel\n'
                            f'3 - Tesoura\n')

    escolha_bot = random.choice(bot_escolha_random)
    try:
        if escolha_usuario == '1':
            if escolha_bot == 'Pedra':
                print(f'Você escolheu Pedra e o BOT {escolha_bot}')
                print('Empatou!!')
            elif escolha_bot == 'Papel':
                print(f'Você escolheu Pedra e o BOT {escolha_bot}')
                print('Você Perdeu!!')
            else:
                print(f'Você escolheu Pedra e o BOT {escolha_bot}')
                print('Você GANHOU!!')
        elif escolha_usuario == '2':
            if escolha_bot == 'Pedra':
                print(f'Você escolheu Papel e o BOT {escolha_bot}')
                print('Você GANHOU!!!')
            elif escolha_bot == 'Papel':
                print(f'Você escolheu Papel e o BOT {escolha_bot}')
                print('EMPATOU!!!')
            else:
                print(f'Você escolheu Papel e o BOT {escolha_bot}')
                print('Você PERDEU!!!')
        elif escolha_usuario == '3':
            if escolha_bot == 'Pedra':
                print(f'Você escolheu Tesoura e o BOT {escolha_bot}')
                print(f'Você PERDEU!!')
            elif escolha_bot == 'Papel':
                print(f'Você escolheu Tesoura e o BOT {escolha_bot}')
                print(f'Você GANHOU!!')
            else:
                print(f'Você escolheu Tesoura e o BOT {escolha_bot}')
                print(f'EMPATOU!!')
        else:
            print('Escolha uma opção válida')
            print()
            continue
    except:
        print('Ocorreu um erro inexperado.')

    continuar = input('Você quer continuar jogando? [S] Pressione qualquer tecla.\n'
                      '                             [N] Pressione N. ')
    if continuar.lower() == 'n':
        break
