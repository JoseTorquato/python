maior = -999
menor = 999
soma = 0
for i in range(1, 11):
    valor = int(input(f'{i} - Digite um valor: '))
    if valor > 0:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
        soma = soma + valor
    else:
        valor = int(input('Digito informe um valor.'))
print(f'Menor valor = {menor}')
print(f'Maior valor = {maior}')
print(f'Média da soma dos valores = {soma/10}')