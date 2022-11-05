import math

n1 = float(input('Digite primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))


class Calculadora:

    def Adição(self, n1, n2):
        return n1 + n2

    def Subtração(self, n1, n2):
        return n1 - n2

    def Potencia(self, n, expoente):
        return n ** expoente

    def primeiro_vs_quadrado_do_segundo(self, n1, n2):
        return n1 * pow(n2, 2)

    def soma_dos_quadrados(self, n1, n2):
        return pow(n1, 2) + pow(n2, 2)

    def RaizQuadrada(self, n):
        return math.sqrt(n)

    def Seno(self, n):
        return math.sin(n)

    def Multiplicação(self, n1, n2):
        return n1 * n2


calculadora = Calculadora()
a = calculadora.Adição(n1, n2)
quadrado_n1 = calculadora.Potencia(n1, 2)
quadrado_n2 = calculadora.Potencia(n2, 2)
b = calculadora.Multiplicação(n1, quadrado_n2)
c = quadrado_n1
soma_dos_quadrados = quadrado_n1 + quadrado_n2
d = calculadora.RaizQuadrada(soma_dos_quadrados)
e = calculadora.Seno(calculadora.Subtração(n1, n2))


print('a)' + str(a))
print('b)' + str(b))
print('c)' + str(c))
print('d)' + str(d))
print('e)' + str(e))
