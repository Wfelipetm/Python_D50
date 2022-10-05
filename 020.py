'''Vamos fazer um programa que fique lendo uma sequência de palavras digitadas pelo usuário, uma a uma,
   até que o usuário diga que finalizou a entrada de palavras.
   Armazene as palavras digitadas pelo usuário em uma lista.
   Após o usuário finalizar a digitação, percorra a lista e procure pela maior palavra.
   Se mais de uma palavra empatar em tamanho, imprima todas elas!'''


def lerPalavra(palavras):
    palavra = input("\n Digite uma palavra: ")
    palavras.append(palavra)


def perguntarContinuarLeitura():
    retorno = ''
    while (retorno != 's' and retorno != 'n'):
        retorno = input('Continuar lendo ? [s]im/[n]ao: ')
    return retorno == 's'


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


def imprimeResultado(maioresPalavras):
    mensagem = "\n\n"
    multiplasPalavras = len(maioresPalavras) > 1
    if multiplasPalavras:
        mensagem += 'As maiores palavras são: '
    else:
        mensagem += 'A maior palavra é: '
        print(mensagem)
    for palavra in maioresPalavras:
        print(palavra)


def main():
    palavras = []
    continuarLendo = True
    while (continuarLendo):
        lerPalavra(palavras)
        continuarLendo = perguntarContinuarLeitura()
    ordenaPalavrasPorTamanhoEmOrdemDescrescente(palavras)

    maioresPalavras = []
    preencheMaioresPalavras(palavras, maioresPalavras)
    imprimeResultado(maioresPalavras)


main()
