from faker import Faker

falso = Faker('pt_BR')
Faker.seed(0)
while True:

    for c in range(50):
        numero_secreto = falso.pyint(1, 50)
    # print(numero_secreto)

    # numero_secreto = 42
    total_de_tentativas = 4
    rodada = 1

    while total_de_tentativas > 0:
        print('--------------------------------------------')
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
        chute = int(input('Tente adivinhar o número que eu pensei!: '))

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Parabéns, voce acertou!")
            break
        elif maior:
            print(f'O seu numero é maior, tente um numero menor que: {chute}')
        elif menor:
            print(f'O seu numero é menor, tente um numero maior que: {chute}')

        # rodada = rodada + 1 # roda sem limite de tentativas.
        total_de_tentativas = total_de_tentativas - 1

    print("Fim do jogo")

    sair = input('Deseja continuar no Game? [s]im ou [n]ão: ')
    if sair == 'n':
        break
