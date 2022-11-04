'''Vamos fazer um codificador de string simples.
Leia um texto digitado pelo usuário e desloque cada caractere 3 posições para a direita.
No final imprima a string codificada.'''



def LerTextoUsuario(mensagem):
    texto = input(mensagem)
    return texto


def CodificaTexto(textoOriginal):
    textoCodificado = ""
    for letra in textoOriginal:
        textoCodificado += chr(ord(letra) + 3)
    return textoCodificado


def main():
    textoOriginal = LerTextoUsuario("Digite um texto:")
    textoCodificado = CodificaTexto(textoOriginal)

    print('Texto codificado: ' + textoCodificado)


main()
