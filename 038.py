'''Vamos fazer uma função que receba um ano por parâmetro 
e retorne se este ano é bissexto ou não.
Para determinar se um ano é bissexto você deve verificar:
Se o ano é divisível por 4 e não é divisível por 100 OU
Se o ano é divisível por 4, por 100 e por 400

Faça um programa que leia um ano, utilize a função criada e 
imprima o resultado na tela para o usuário, dizendo se o ano é bissexto ou não.'''





def DesejaContinuar():
    continuar = input('Deseja continuar? [s]im/[n]ao: ')
    return continuar == "s"


def EhBissexto(ano):
    divisivelPor4 = (ano % 4) == 0
    divisivelPor100 = (ano % 100) == 0
    divisivelPor400 = (ano % 400) == 0

    divisivelPor4ENaoPor100 = divisivelPor4 and not divisivelPor100
    divisivelPorTudo = divisivelPor4 and \
        divisivelPor100 and \
        divisivelPor400
    return divisivelPor4ENaoPor100 or divisivelPorTudo


def ImprimeResultado(ano, ehBissexto):
    msg = "O ano {ano}{nao} e bissexto!".format(ano=ano,
                                                nao=" nao" if not ehBissexto else "")
    print(msg)


def main():
    continuar = True
    while continuar:
        ano = int(input('Digite um ano: '))

        ImprimeResultado(ano, EhBissexto(ano))
        continuar = DesejaContinuar()


main()
