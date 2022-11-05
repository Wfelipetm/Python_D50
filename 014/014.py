frase = input('Digite uma frase: ')
print()


def quantidade_string(string):
    string = len(frase)
    return string


def conta_pontuação(string):
    string = string.lower()
    pontuação = ',!'
    return sum(string.count(i) for i in pontuação)


def conta_pontuação(string):
    string = string.lower()
    número = '0123456789'
    return sum(string.count(i) for i in número)


def conta_vogais(string):
    string = string.lower()
    vogais = 'aeiou'
    return sum(string.count(i) for i in vogais)


q = quantidade_string(frase)
p = conta_pontuação(frase)
n = conta_pontuação(frase)
v = conta_vogais(frase)


print(f'a) Quantidade caracteres tem a string: {q}')
print(f'b) Quantidade caracteres são de pontuação: {p}')
print(f'c) Quantidade caracteres são de número: {n}')
print(f'd) Quantidade de caracteres vogais: {v}')
