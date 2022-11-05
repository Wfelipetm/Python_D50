def leia_valor_da_temperatura(c):
    valor = -1
    while (valor <= 0):
        valor = float(input(c))
    return valor


tc = leia_valor_da_temperatura('Informe a temperatura em °C: ')
tf = tc * 1.8 + 32
print(f'A temperatura de {tc}°C corresponde a {tf}°F!')


tf = leia_valor_da_temperatura('Informe a temperatura em °F: ')
tc = (tf - 32) * 5 / 9
print(f'A temperatura de {tf}°F corresponde a {tc}°C!')
