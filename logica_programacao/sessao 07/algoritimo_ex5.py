nome = input('Qual o nome do usuário: ')
senha = input('Qual a sua senha: ')


while nome == senha:
    print('Usuário e senha deveram ser diferentes.')
    print()
    nome = input('Qual o nome do usuário: ')
    senha = input('Qual a sua senha: ')
print(f'Seja bem-vindo {nome}!')

