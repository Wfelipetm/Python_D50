'''Vamos continuar o código do desafio 20!
Para este desafio vamos criar uma função que lê a sequência de palavras de um arquivo texto chamado input.txt e 
armazena essas palavras lidas em uma lista (a mesma utilizada no desafio anterior).
Após feita esta leitura, faça a mesma coisa que no desafio 20.
No final, escreva a (ou as) palavra com o maior tamanho em um outro arquivo chamado output.txt'''


def lerPalavrasDoArquivo(palavras):
    input_file = open("input.txt", "r")
    conteudo = input_file.readlines()
    input_file.close()

    for linha in conteudo:
        palavrasDaLinha = linha.split()
        palavras += palavrasDaLinha


def ordenaPalavrasPorTamanhoEmOrdemDescrescente(palavras):
    palavras.sort(key=len, reverse=True)


def preencheMaioresPalavras(palavras, maioresPalavras):
    tamanhoMaiorPalavra = len(palavras[0])
    for palavra in palavras:
        tamanhoPalavra = len(palavra)
        if tamanhoPalavra == tamanhoMaiorPalavra:
            maioresPalavras.append(palavra)
        else:
            break


def escreveNoArquivoDeSaida(maioresPalavras):
    mensagem = "\n\n"

    multiplasPalavras = len(maioresPalavras) > 1
    if multiplasPalavras:
        mensagem += 'As maiores palavras são: '
    else:
        mensagem += 'A maior palavra é: '

    output_file = open("output.txt", "w")
    output_file.write(mensagem + "\n")

    for palavra in maioresPalavras:
        output_file.write(palavra)
        output_file.write("\n")
    output_file.close()


def main():
    palavras = []

    lerPalavrasDoArquivo(palavras)

    ordenaPalavrasPorTamanhoEmOrdemDescrescente(palavras)

    maioresPalavras = []

    preencheMaioresPalavras(palavras, maioresPalavras)

    escreveNoArquivoDeSaida(maioresPalavras)


main()
