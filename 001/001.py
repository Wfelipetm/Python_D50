Produto = int(input('Valor do produto: '))
valorProduto = Produto
Dinheiro = int(input('Valor do Cliente: '))
valorCliente = Dinheiro

print(f'Seu troco: {valorCliente - valorProduto}')

if valorCliente < valorProduto:
    print('Valor insuficiente')

else:
    print('Volte sempre')
