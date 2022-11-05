'''Agora leia um arquivo texto contendo várias frases e utilize a função gerada no desafio 45.
Como resultado escreva outro arquivo de saída com o texto embaralhado.

Tente ler o texto gerado como resultado.
Vcoê vreá que o seu crbéreo é cpaaz de ler o ttxeo se memianvrtos a piremria e a úilmta lrtea iátntca.'''


import random


def LeTextoDoArquivo(nomeDoArquivo):
    input_file = open(nomeDoArquivo, 'r')
    texto = input_file.read()
    input_file.close()
    return texto


def EscreveTextoNoArquivo(texto, nomeDoArquivo):
    output_file = open(nomeDoArquivo, 'w')
    output_file.write(texto)
    output_file.close()


def EmbaralhaPalavraMantendoPrimeiraUltima(palavra):
    tamanhoPalavra = len(palavra)
    novaPalavra = palavra
    if tamanhoPalavra > 1:
        meio = palavra[1:tamanhoPalavra-1]
        novoMeio = ''.join(random.sample(meio, len(meio)))
        novaPalavra = palavra[0] + novoMeio + palavra[tamanhoPalavra-1]
    return novaPalavra


def main():
    texto = LeTextoDoArquivo('entrada.txt')
    novoTexto = ""
    for palavra in texto.split(' '):
        novoTexto += EmbaralhaPalavraMantendoPrimeiraUltima(palavra) + ' '

    EscreveTextoNoArquivo(novoTexto, 'saida.txt')


main()
