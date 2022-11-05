'''Vamos fazer o sistema de codificação e decodificação de arquivos textos.
Para este desafio vamos utilizar as funções criadas nos desafios 39, 30, 31 e 32, 
além daquelas de leitura e escrita de arquivos que utilizamos no desafio 21.
Escrevi a sequência da implementação para facilitar o desenvolvimento do desafio.
1) Leia o texto de um arquivo entrada.txt
2) Codifique o texto com a função do desafio 31
3) Utilize a função do desafio 29, substituindo as vogais do texto codificado por *
4) Escreva o texto codificado em um arquivo cod.txt e a sequência de vogais em um outro arquivo chave.txt
5) Agora leia os arquivos cod.txt e chave.txt e utilize a função do desafio 30 para substituir os * pelas vogais
6) Pegue o resultado e utilize a função do desafio 32 para decodificar a string e escrever o resultado no arquivo saida.txt'''





def LeTextoDoArquivo(nomeDoArquivo):
    input_file = open(nomeDoArquivo, 'r')
    texto = input_file.read()
    input_file.close()
    return texto


def EscreveTextoNoArquivo(texto, nomeDoArquivo):
    output_file = open(nomeDoArquivo, 'w')
    output_file.write(texto)
    output_file.close()


def EhVogal(letra):
    return letra in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def CensuraTexto(texto):
    textoCensurado = ""
    vogais = ""
    for i in range(len(texto)):
        if EhVogal(texto[i]):
            textoCensurado += '*'
            vogais += texto[i]
        else:
            textoCensurado += texto[i]
    return textoCensurado, vogais


def RemoveCensuraTexto(textoCensurado, vogais):
    contadorVogais = 0
    textoOriginal = ""
    for i in range(len(textoCensurado)):
        if textoCensurado[i] == '*':
            textoOriginal += vogais[contadorVogais]
            contadorVogais += 1
        else:
            textoOriginal += textoCensurado[i]
    return textoOriginal


def CodificaTexto(textoOriginal):
    textoCodificado = ""
    for letra in textoOriginal:
        if letra == '\n':
            textoCodificado += letra
        else:
            textoCodificado += chr(ord(letra) + 3)
    return textoCodificado


def DecodificaTexto(textoCodificado):
    textoOriginal = ""
    for letra in textoCodificado:
        if letra == '\n':
            textoOriginal += letra
        else:
            textoOriginal += chr(ord(letra) - 3)
    return textoOriginal


def EfetuaCodificacaoDoArquivo(texto):
    textoCodificado = CodificaTexto(texto)
    textoCensurado, vogais = CensuraTexto(textoCodificado)

    EscreveTextoNoArquivo(textoCensurado, 'cod.txt')
    EscreveTextoNoArquivo(vogais, 'chave.txt')


def DecodificaTextos():
    textoCensurado = LeTextoDoArquivo('cod.txt')
    vogais = LeTextoDoArquivo('chave.txt')
    textoSemCensura = RemoveCensuraTexto(textoCensurado, vogais)
    textoOriginal = DecodificaTexto(textoSemCensura)
    return textoOriginal


def main():
    texto = LeTextoDoArquivo('entrada.txt')

    EfetuaCodificacaoDoArquivo(texto)
    textoDecodificado = DecodificaTextos()

    EscreveTextoNoArquivo(textoDecodificado, 'saida.txt')


main()
