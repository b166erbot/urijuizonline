# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

from math import factorial

def calcular(x):
    return x[1] * factorial(x[0])


def para_numeral(amc): # str
    unidades = enumerate(map(int, amc[::-1]), 1)
    return sum(map(calcular, unidades))


def main():
    entrada = input()
    while entrada != '0':
        print(para_numeral(entrada))
        entrada = input()


if __name__ == '__main__':
    main()
