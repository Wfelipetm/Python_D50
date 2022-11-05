def calcula_fatorial(numero):
    if numero == 0:
        return 1
    return numero * calcula_fatorial(numero-1)


def calcula_fatorial_laco(numero):
    fatorial = 1
    for n in range(1, numero + 1):
        fatorial *= n
    return fatorial


def leia_numero_inteiro_positivo():
    numero = -1
    while (numero < 0):
        numero = int(input('Digite um numero inteiro positivo: '))
    return numero


numero = leia_numero_inteiro_positivo()
fatorial = calcula_fatorial(numero)
fatorial_com_laco = calcula_fatorial_laco(numero)

print('Fatorial de {n} é {fat}'.format(n=numero, fat=fatorial))
print('Fatorial_com_laco de {n} é {fat}'.format(
    n=numero, fat=fatorial_com_laco))
