while True:
    print()
    num_1 = input('digite um número:')
    operadores = input('Digite um operador: ')
    num_2 = input('Digite um número: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número. ')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *

    if operadores == '+':
        print(num_1 + num_2)

    elif operadores == '-':
        print(num_1 - num_2)

    elif operadores == '/':
        print(num_1 / num_2)

    elif operadores == '*':
        print(num_1 * num_2)

    elif operadores == '**':
        print(num_1 ** num_2)

    else:
        print('Operador invalido')
    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break
