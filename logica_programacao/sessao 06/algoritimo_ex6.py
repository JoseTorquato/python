hora_excedente = 0

hora_trabalhada = int(input('Quantas horas voce trabalhou: '))

if hora_trabalhada > 50:
    hora_excedente = hora_trabalhada - 50
    hora_trabalhada -= hora_excedente
    extra_pagar = hora_excedente * 20
    salario_normal = hora_trabalhada * 10
    salario_total = extra_pagar + salario_normal
    print(f'Você trabalhou {hora_trabalhada+hora_excedente} horas e vai receber o total R${salario_total:.2f}.\n'
          f'Valor recebido pelas horas extra({hora_excedente}), R${extra_pagar:.2f}.')
else:
    salario = hora_trabalhada * 10
    print(f'Você trabaalhou {hora_trabalhada} horas e vai receber R$ {salario:.2f}.')