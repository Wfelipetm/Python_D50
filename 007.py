'''Faça um programa que leia o peso e a altura 
 de uma pessoa e calcule o IMC dela, imprimindo o valor 
 calculado e em qual faixa essa pessoa se encontra.'''


def leia_valor_positivo(mensagem):
    valor = -1
    while (valor <= 0):
        valor = float(input(mensagem))
    return valor


peso = leia_valor_positivo('Digite seu peso: ')
altura = leia_valor_positivo('Digite sua altura: ')
imc = peso / altura ** 2
# imc = peso / pow(altura, 2)


mensagem = ""
if (imc < 18.5):
    mensagem = 'Magreza'
elif (imc <= 18.5 and imc < 25.0):
    mensagem = 'Normal'
elif (imc <= 25.0 and imc < 30.0):
    mensagem = 'Sobrepeso'
elif (imc <= 30.0 and imc < 40.0):
    mensagem = 'Obesidade'
else:
    mensagem = 'Obsidade grave'

# formatação IPC - por casas!
print('O valor do IMC calculado é  {:.3f}'.format(imc))
print('Sua categoria de IMC é : ' + mensagem)
