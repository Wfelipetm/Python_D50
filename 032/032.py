'''Vamos fazer um decodificador simples de strings.
Agora vamos fazer o processo inverso do desafio 31. Lendo uma string já codificada pelo usuário 
(utilizando o algoritmo do desafio 31) você irá fazer o processo inverso para decodificá-la, 
subtraindo 3 de cada letra e descobrindo o texto original.'''



No final imprima o texto decodificado na tela.

def LerTextoUsuario(mensagem):
    texto = input(mensagem)
    return texto


def DecodificaTexto(textoCodificado):
    textoOriginal = ""
    for letra in textoCodificado:
        textoOriginal += chr(ord(letra) - 3)
    return textoOriginal


def main():
    textoCodificado = LerTextoUsuario("Digite um textoCodificado: ")
    textoDecodificado = DecodificaTexto(textoCodificado)

    print('Texto decodificado: ' + textoDecodificado)


main()
