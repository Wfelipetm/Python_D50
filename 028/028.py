'''Vamos fazer um programa que leia um texto digitado pelo usuário e imprima na tela se o texto digitado é palíndromo ou não!
Para um texto ser palíndromo, ele pode ser lido da mesma maneira nos dois sentidos: da frente para trás e de trás para frente.
Exemplos de palavras palíndromas: Anna, Otto, Reviver, Osso.
Mas também podem ser frases como: “Socorram-me, subi no ônibus em Marrocos'''



import unicodedata


def RemovePontuacao(texto):
    textoEditado = texto.replace(' ', '')
    textoEditado = textoEditado.replace('.', '')
    textoEditado = textoEditado.replace(',', '')
    textoEditado = textoEditado.replace('!', '')
    textoEditado = textoEditado.replace('?', '')
    textoEditado = textoEditado.replace('-', '')
    textoEditado = textoEditado.replace(':', '')
    textoEditado = textoEditado.replace(';', '')
    return textoEditado


def RemoveAcentuacao(texto):
    normalized = unicodedata.normalize('NFD', texto)
    return normalized.encode('ascii', 'ignore').decode('utf8').casefold()


def NormalizaTexto(texto):
    textoEditado = RemovePontuacao(texto)
    textoEditado = RemoveAcentuacao(textoEditado)
    return textoEditado


def EhPalindromo(texto):
    texto = NormalizaTexto(texto)
    inicioTexto = 0
    fimTexto = len(texto) - 1

    while inicioTexto < fimTexto:
        if texto[inicioTexto] != texto[fimTexto]:
            return False
        inicioTexto += 1
        fimTexto -= 1
    return True


def main():
    texto = input('Digite um texto: ')
    ehPalindromo = EhPalindromo(texto)

    naoEh = "" if ehPalindromo else "não "
    mensagem = "O texto {}é palíndromo!".format(naoEh)
    print(mensagem)


main()
