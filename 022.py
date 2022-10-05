def LeiaEntradaUsuario():
    print('O fornato da  entrada  deve ser o sequinte: ')
    print('[1, 2, 3, 4, ..., 30]')
    entrada = input(' Digite una lista de inteiros: ')
    return entrada


def RemoveColcheteEspacosDaString(entrada):
    entrada = entrada.replace(']', '')
    entrada = entrada.replace('[', '')
    entrada = entrada.replace(' ', '')
    return entrada


def ConverteListastringsParaInteiros(entrada):
    entrada = RemoveColcheteEspacosDaString(entrada)

    inteirosEntrada = []
    if (len(entrada) > 0):
        entrada = entrada.split(',')

        for palavra in entrada:
            inteirosEntrada.append(int(palavra))
    return inteirosEntrada


def EfetuaOperacoes(inteiros):
    if len(inteiros) > 0:
        soma = 0
        menor = maior = inteiros[0]

        for i in inteiros:
            soma += i
            if i < menor:
                menor = i
            if i > maior:
                maior = i

        media = soma / len(inteiros)
        print("O maior valor é " + str(maior))
        print("O menor valor é " + str(menor))
        print("O média dos valor é " + str(media))

    else:
        print('Lista esta vazia')


def main():
    entrada = LeiaEntradaUsuario()
    inteirosEntrada = ConverteListastringsParaInteiros(entrada)
    EfetuaOperacoes(inteirosEntrada)


main()
