def le_quantidade_de_moeda(nomeMoeda):
    quantidade = -1
    while (quantidade < 0):
        quantidade = int(input(nomeMoeda + " : "))
    return quantidade


print('Hey Arthur, me diga quantas moedas de cada valor voce tem? ')

quantUm = le_quantidade_de_moeda("1 centavo")
quantCinco = le_quantidade_de_moeda("5 centavo")
quantDez = le_quantidade_de_moeda("10 centavo")
quantVinteCinco = le_quantidade_de_moeda("25 centavo")
quantCinquenta = le_quantidade_de_moeda("50 centavo")
quantUmReal = le_quantidade_de_moeda("1 real")

valorTotal = quantUm * 0.01
valorTotal += quantCinco * 0.05
valorTotal += quantDez * 0.10
valorTotal += quantVinteCinco * 0.25
valorTotal += quantCinquenta * 0.50
valorTotal += quantUmReal

print('Arthur você tem R$ {:.2f}'.format(valorTotal))
