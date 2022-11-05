'''Faça um programa que leia a quantidade de dias 
trabalhados pelo funcionario e imprima 
essa informação convertida em anos, meses e dias.
considerando que todos os meses possuem sempre 30 dias.'''

msg = 'Digite a quantidade de dia trabalhado: '
dias_trabalhado = -1
while (dias_trabalhado <= 0):
    dias_trabalhado = int(input(msg))

anos = 0
while ((dias_trabalhado - 365) >= 0):
    dias_trabalhado -= 365
    anos = anos + 1

meses = 0
while ((dias_trabalhado - 30) >= 0):
    dias_trabalhado = dias_trabalhado - 30
    meses += 1


print(f'{anos} anos, {meses} meses, {dias_trabalhado} dias')
