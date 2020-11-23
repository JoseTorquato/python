num_1 = int(input('Qual numero vocÊ gostaria de ver a tabuada: '))

print(f'Tabuada do {num_1}')
print()
i = 1
while i <= 10:
    valor = num_1 * i
    print(f'{num_1} X {i} = {valor}')
    i += 1
