'''Vamos incrementar o desafio anterior adicionando um menu no nosso sistema.
No menu você vai dar a opção para o usuário escolher o tipo de relatório que ele quer criar.
Por padrão o relatório será gerado na mesma ordem de leitura do arquivo ‘usuarios.txt’, conforme fizemos no desafio anterior.
Adicionaremos uma segunda opção onde o relatório será gerado com os usuários ordenados em ordem de utilização de armazenamento.
Leia também o nome do arquivo de relatório a ser gerado (por padrão o sistema gera “relatório.txt”).'''


import os

MEGABYTE = 1024*1024
PADRAO = 1
ORDENADO = 2
usuarios = {}


def LeTextoDoArquivo(nomeDoArquivo):
    input_file = open(nomeDoArquivo, 'r')
    texto = input_file.read()
    input_file.close()
    return texto


def EscreveTextoNoArquivo(texto, nomeDoArquivo):
    output_file = open(nomeDoArquivo, 'w')
    output_file.write(texto)
    output_file.close()


def PreencheInformacoesUsuarios(texto):
    linhas = texto.split('\n')
    for linha in linhas:
        linhaEmLista = linha.split()
        nomeUsuario = linhaEmLista[0]
        espacoUtilizado = int(linhaEmLista[1])
        usuarios[nomeUsuario] = espacoUtilizado


def CalculaEspacoTotal():
    espacosUtilizados = [espacoDoUsuario for _,
                         espacoDoUsuario in usuarios.items()]
    espacoTotal = sum(espacosUtilizados)
    return espacoTotal


def ConverteBytesParaMegabytes(espacoEmBytes):
    return espacoEmBytes / MEGABYTE


def CriaRelatorio():
    quantidadeUsuarios = 0
    espacoTotal = CalculaEspacoTotal()

    relatorio = 'ACME Inc.    Uso do espaço em disco pelos usuários\n'
    relatorio += '----------------------------------------------------\n'
    relatorio += 'Nr.  Usuário        Espaço utilizado     % do uso\n'

    numero = 1
    for nomeUsuario, espacoDoUsuario in usuarios.items():
        espacoEmMB = ConverteBytesParaMegabytes(espacoDoUsuario)
        porcentagem = espacoDoUsuario*100/espacoTotal

        textoNumero = str(numero).ljust(5)
        textoNome = nomeUsuario.ljust(14)
        textoEspaco = "{:.2f}".format(espacoEmMB).rjust(7) + " MB"
        textoEspaco += " ".ljust(11)
        textoPorc = "{:.2f}".format(porcentagem).rjust(6) + "%"

        linha = "{num}{usuario}{espaco}{porc}\n".format(num=textoNumero,
                                                        usuario=textoNome,
                                                        espaco=textoEspaco,
                                                        porc=textoPorc)
        relatorio += linha
        quantidadeUsuarios += 1
        numero += 1

    espacoTotalEmMB = ConverteBytesParaMegabytes(espacoTotal)
    relatorio += "\nEspaco total ocupado: {:.2f} MB".format(espacoTotalEmMB)
    relatorio += "\nEspaco médio ocupado: {:.2f} MB".format(
        espacoTotalEmMB / quantidadeUsuarios)
    return relatorio


def LeOpcaoDoUsuario():
    opcaoInvalida = True
    opcao = -1
    while opcaoInvalida:
        ImprimeMenu()
        opcao = int(input('Digite a opcao: '))
        opcaoInvalida = opcao < PADRAO or opcao > ORDENADO
        if opcaoInvalida:
            os.system("cls")
            print('\n  OPCAO INVALIDA! \n')

    return opcao


def ImprimeMenu():
    print('---------------------------------------------------')
    print(' Gerador de relatório de armazenamento por usuário ')
    print('---------------------------------------------------')
    print('Escolha uma das opções: ')
    print('  1) Gerar relatório padrão.')
    print('  2) Gerar relatório ordenado por utilização.')
    print('---------------------------------------------------')


def LeNomeDoRelatorio():
    nomeDoRelatorio = input("Digite o nome do relatorio: ")
    if len(nomeDoRelatorio) == 0:
        nomeDoRelatorio = "relatorio"
    return nomeDoRelatorio + ".txt"


def OrdenaInformacoesPorArmazenamento():
    global usuarios
    usuarios = {chave: valor for chave, valor in sorted(usuarios.items(),
                                                        key=lambda item: item[1])}


def main():
    opcaoDoUsuario = LeOpcaoDoUsuario()
    nomeRelatorio = LeNomeDoRelatorio()

    texto = LeTextoDoArquivo('usuarios.txt')
    PreencheInformacoesUsuarios(texto)

    if opcaoDoUsuario == ORDENADO:
        OrdenaInformacoesPorArmazenamento()

    relatorio = CriaRelatorio()
    EscreveTextoNoArquivo(relatorio, nomeRelatorio)


main()
