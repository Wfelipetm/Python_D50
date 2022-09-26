# Faça um programa que leia uma string e imprima:
# a) Quantidade caracteres tem a string.
# b) Quantidade caracteres são de pontuação....')
# c) Quantidade caracteres são de número.
# d) Quantidade caracteres quantos são vogais.

frase = input('Digite uma frase: ')
print()


quantidade_string = len(frase)
print(f'a) Quantidade caracteres tem a string: {quantidade_string}')


def conta_pontuação(string):
    string = string.lower()
    pontuação = ',!'
    return sum(string.count(i) for i in pontuação)


p = conta_pontuação(frase)
print(f'b) Quantidade caracteres são de pontuação: {p}')


def conta_pontuação(string):
    string = string.lower()
    número = '0123456789'
    return sum(string.count(i) for i in número)


n = conta_pontuação(frase)
print(f'c) Quantidade caracteres são de número: {n}')


def conta_vogais(string):
    string = string.lower()
    vogais = 'aeiou'
    return sum(string.count(i) for i in vogais)


v = conta_vogais(frase)
print(f'd) Quantidade de caracteres vogais: {v}')
