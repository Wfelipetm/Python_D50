'''Vamos fazer um programa que converte texto em português para código morse.
Leia um texto digitado pelo usuário e utilize um mapeamento para fazer a conversão do texto para morse.'''

import dicionario_morse


def main():
    texto = input('Digite um texto: ')
    texto = texto.lower()

    textoMorse = ""
    for letra in texto:
        textoMorse += dicionario_morse.morseMap[letra] + " "
    print(textoMorse)

    # OU TAMBÉM PODEMOS USAR COMPREHENSIONS
    listaLetrasMorse = [dicionario_morse.morseMap[i] for i in texto]
    textoMorse2 = " ".join(listaLetrasMorse)
    print(textoMorse2)


main()
