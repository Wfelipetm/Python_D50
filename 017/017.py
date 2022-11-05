print("--------------------------------------------")


def leia_valor_positivo(mensagem):
    valor = -1
    while (valor < 0):
        valor = float(input(mensagem))
    return valor


nome_funcionario = input('Digite o nome do funcionario: ')
dias_trabalhados = leia_valor_positivo('Dias trabalhados: ')
dependente = leia_valor_positivo('Quantos dependentes: ')


def salario_bruto():
    return 23.0 * dias_trabalhados + dependente * 34.0


def desconto_inss():
    return 0.085 * salario_bruto()


def desconto_ir():
    return 0.15 * salario_bruto()


print("-------------------------------------------")
print(f'Nome do funcionario: {nome_funcionario}')
print(f'Salário bruto: R${salario_bruto()}')
print(f'Desconto INSS: R${desconto_inss()}')
ir = desconto_ir()
print('Desconto IR: R${:.2f}'.format(ir))
valor_liquido = salario_bruto() - desconto_inss() - desconto_ir()
print(f'Salário Liquido: R${valor_liquido}')
print("-------------------------------------------")
