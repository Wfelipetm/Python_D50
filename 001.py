'''Faça um programa que entre o preço de um produto e o valor em dinheiro pago.
imprima para o usuário o quanto será o troco.'''

Produto = int(input('Valor do produto: '))
valorProduto = Produto
Dinheiro = int(input('Valor do Cliente: '))
valorCliente = Dinheiro

print(f'Seu troco: {valorCliente - valorProduto}')

if valorCliente < valorProduto:
    print('Valor insuficiente')

else:
    print('Volte sempre')
