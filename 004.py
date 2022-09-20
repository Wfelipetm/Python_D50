'''Faça um programa que receba duas dimenões de um 
terreno e imprima a área deste terreno.considerando 
que o preço do metro quadrado é de 7.592,00 , imprima 
também o valor que custará este terreno'''


frente = float(input('Qual a medida da frente do terreno? '))
fundos = float(input('Qual o fundos do terreno? '))
valorm2 = 7592.00
area = frente * fundos
valorterreno = valorm2 * area

print('A área do terreno é: ' + str(area))
print('Valor do terreno é: ' + str(valorterreno))
