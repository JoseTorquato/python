g1 = 'Grupo 1'
g2 = 'Grupo 2'

while True:
    poluicao = float(input('Qual o indice de poluição? '))

    if poluicao:
        poluicao = float(poluicao)

        if poluicao == 0.3 and poluicao < 0.4:
            print(f'Intimar {g1}')
        elif poluicao == 0.4 and poluicao < 0.5:
            print(f'Intimar {g1} e {g2}, a suspenderem as atividades.')
        elif poluicao >= 0.5:
            print(f'{g1} e {g2} tem que parlisarem suas atividades.')
        else:
            print('Níveis aceitaveis')
    else:
        print('Digite um número válido. Exemplo: [0.3]')