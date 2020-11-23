excesso = 0
multa = 0

peso_peixe = float(input('QUantos kilos foram pescados hoje: '))

if peso_peixe > 50:
    excesso = peso_peixe - 50
    multa = excesso * 4
    print(f'Você pescou {peso_peixe} e excedeu o peso limite de 50 KG.\n'
          f'A multa a ser paga é de R$ {multa:.2f}.')
else:
    print(f'Você pescou {peso_peixe:.2f}KG.')