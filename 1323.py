# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


class Tabela:
    def __init__(self, lado):
        self.lado = lado

    def calcular(self):
        quadrados = pow(self.lado, 2)
        temp = sum((pow(self.lado - x, 2) for x in range(1, self.lado + 1)))
        return quadrados + temp


def main():
    entrada = int(input())
    while entrada != 0:
        print(Tabela(entrada).calcular())
        entrada = int(input())


if __name__ == '__main__':
    main()
