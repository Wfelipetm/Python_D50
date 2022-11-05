'''Um professor quer separar sua turma em duplas e gostaria de um programa para fazer isso.
Escreva um programa que leia o nome dos alunos e imprima os possíveis grupos que podem ser formados. Não imprima duplas repetidas.'''


from itertools import combinations

nomeDosAlunos = []


def LeNomeDosAlunos():
    quantidade = int(input('Quantos alunos você tem? '))

    for i in range(quantidade):
        mensagem = 'Digite o nome do aluno ' + str(i+1) + ": "
        nome = input(mensagem)
        nomeDosAlunos.append(nome)


def CriaPossiveisGrupos():
    comb = combinations(nomeDosAlunos, 2)
    return comb


def main():
    LeNomeDosAlunos()
    possiveisGrupos = CriaPossiveisGrupos()

    for grupo in list(possiveisGrupos):
        print(grupo)


main()
