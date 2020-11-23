while True:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite um número: '))
    num3 = int(input('Digite um número: '))
    num4 = int(input('Digite um número: '))

    pot1 = num1 ** 2
    pot2 = num2 ** 2
    pot3 = num3 ** 2
    pot4 = num4 ** 2

    if pot3 >= 1000:
        print('Terceiro número acima de 1000, valor deu:', pot3)
        break
    else:
        print(pot1)
        print(pot2)
        print(pot3)
        print(pot4)