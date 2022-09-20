'''Faça um programa que receba o valor dos 
  catetos de um triângulo retângulo e 
  improma na tela o valor da Hipotenusa. '''

import math


def leia_valor_cateto_positivo(nome_cateto):
    mensagem = 'Digite o valor do cateto' + nome_cateto + ':'
    valor_cateto = -1
    while (valor_cateto <= 0):
        valor_cateto = float(input(mensagem))
    return valor_cateto


a = leia_valor_cateto_positivo('a')
b = leia_valor_cateto_positivo('b')

soma_quadrado_catetos = pow(a, 2) + pow(b, 2)
h = math.sqrt(soma_quadrado_catetos)

print('O valor da hipotenusa do triangulo retangulo é  {:.2f}'.format(h))
