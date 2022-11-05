while True:
    def leia_valor_positivo(mensagem):
        valor = -1
        while (valor < 0):
            valor = int(input(mensagem))
        return valor

    def implementa():
        if n == 2:
            print("2 é primo")
        elif n % 2 == 0:
            print(f"{n} não é primo, pois 2 é o único número par primo.")
        else:
            x = 3
            while (x < n):
                if n % x == 0:
                    break
                x = x + 2
            if x == n:
                print(f"{n} é primo")
            else:
                print(f"{n} não é primo, pois é divisível por {x}")

    print("------------------------------------")
    n = leia_valor_positivo("Digite um número:")
    implementa()
    print("------------------------------------")
    sair = input('Deseja continuar? [s]im ou [n]ão: ')
    if sair == 'n':
        break
