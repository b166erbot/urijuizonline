# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

from functools import reduce
from operator import mul


def cbrt(x):
    return pow(x, 1/3)


def main():
    entradas = list(map(int, input().split()))
    while entradas != [0, 0, 0]:
        resposta = int(cbrt(reduce(mul, entradas)))
        print(resposta)
        entradas = list(map(int, input().split()))


if __name__ == '__main__':
    main()
