'''Faça um programa que leia uma string e um caractere, removendo todas as 
ocorrências este caractere lido da string inicialmente lida.
imprima o resultado da string após a remoção dos caracteres.'''


while True:
    print('--------------------------------------------------------')

    def remove_caractere():
        string = input("Digite uma string: ")
        caracteres = input("Digite uma caracteres para remover:  ")
        for x in range(len(caracteres)):
            string = string.replace(caracteres[x], " ")
        return string

    print(remove_caractere())
    sair = input('Deseja remover outro caractere? [s]im ou [n]ão: ')
    if sair == 'n':
        break

# Eu tenho um coelho que se chama Anestor.
