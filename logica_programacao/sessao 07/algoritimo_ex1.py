num = int(input('Digite um número: '))

maior = 0
while num != 0:
    if num > maior:
        maior = num
    num = int(input('Digite um número: '))
print(f'Maior valor {maior}')