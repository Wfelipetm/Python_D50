'''Faça um programa que receba um número
 inteiro positivo de 1 até N.Imprima na 
 tela o resultado da soma.'''


n = -1
while (n <= 0):
    n = int(input('Digite um numero positivo: '))

soma = 0
for i in range(1, n+1):
    soma += i
print('Valor da soma de 1 até ' + str(n) + ' é ' + str(soma))
