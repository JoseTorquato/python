'''
Simulador de dado
Criar um dado e rolar ele aleatoriamente
Implementar o segundo dado e somar seus resultados
'''

import random

while True:
    def Dado():
        rolou = random.randrange(1, 7)
        return rolou


    jogador_rolou_dado1 = input('Você quer jogar o primeiro dado agora? [S/N] ')

    if jogador_rolou_dado1.upper() == 'S':
        jogou1 = Dado()
        print(jogou1)
    else:
        print('Obrigado por jogar!')
        break

    jogador_rolou_dado2 = input('Você quer jogar o segundo dado agora? [S/N] ')

    if jogador_rolou_dado2.upper() == 'S':
        jogou2 = Dado()
        print(jogou2)
        print(f'A soma dos dois dados deu {jogou1 + jogou2}')
    elif jogador_rolou_dado2.upper() == 'N':
        print(f'A primeira jogada o valor do dado deu {jogou1}.')
        print('Obrigado por jogar!')
        break
    else:
        print('Obrigado por jogar!')
        break

    end_game = input('Você quer continuar jogando? [S/N] ')

    if end_game.upper() == 'S':
        continue
    else:
        print('Obrigado por jogar!')
        break
