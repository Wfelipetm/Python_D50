'''Vamos calcular o salário de um funcionário.
Este funcionário foi contratado em 1995.
No primeiro ano de trabalho, ele recebeu um aumento de 1.5% sobre o salário inicial.
A partir dos próximos anos, a porcentagem de aumento progride em 10% anualmente (1.5%, 1.65%, 1.815%, 1.9965%, 2.196%, ...).
Faça um programa que o usuário digite o salário inicial e o ano que deseja saber o salário.
O programa deve ir calculando os aumentos até chegar no ano desejado e imprimir o salário calculado na tela.'''



salarioInicial = float(input('Digite o salario inicial: R$ '))
anoContratacao = int(input('Digite o ano de contratacao: '))
anoFinal = int(input('Digite o ano que voce quer saber o salario: '))
diferencaAnos = anoFinal - anoContratacao

porcentagem_aumento = 0.015
proporcao_aumento_taxa_anual = 0.10
salario = salarioInicial
for i in range(diferencaAnos):
    salario += salario*porcentagem_aumento
    porcentagem_aumento += porcentagem_aumento*proporcao_aumento_taxa_anual

print('O salario do funcionario em {ano} sera R$ {valor:.2f}'.format(ano=anoFinal,
                                                                     valor=salario))
