''' 
    * Faça um programa que receba o valor do aluguel e a quantidade de dias de atraso. 
      imprima o valor que deverá ser pago.
    
    * Considerando a multa como 3% do valor do aluguel e o juros simples 
      de 0.05% do valor do aluguel por dia de atraso.
'''



while True:
    v_aluguel = float(input("Digite o valor do aluguel: R$ "))
    dias_atraso = float(input("Quantos dias de atraso: "))

    def multa_aluguel():
        return 0.03 * v_aluguel

    def multa_por_dia():
        return dias_atraso * 0.005 * v_aluguel

    valor_a_pagar = v_aluguel + multa_aluguel() + multa_por_dia()
    print('Valor a pagar com juros e multa {:.2f}'.format(valor_a_pagar))

    sair = input('Deseja calcular juros e multa novamante? [s]im ou [n]ão: ')
    if sair == 'n':
        break
