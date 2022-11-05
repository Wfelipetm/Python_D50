'''Agora vamos fazer a famosa sequência de Fibonacci.
Faça um programa que receba um número inteiro e imprima o enésimo termo da sequência de Fibonacci.
Para o desafio se tornar mais interessante preferencialmente tente fazer utilizando recursão.'''


def Fibonacci(posicao):
    if posicao == 0:
        return 0
    if posicao == 1:
        return 1
    return Fibonacci(posicao-1) + Fibonacci(posicao-2)


def main():
    mensagem = 'Digite o elemento de fibonacci que voce deseja: '
    posicao = int(input(mensagem))

    valor = Fibonacci(posicao)

    mensagem = 'O valor de Fibonacci {pos} é {val}'.format(pos=posicao,
                                                           val=valor)
    print(mensagem)


main()
