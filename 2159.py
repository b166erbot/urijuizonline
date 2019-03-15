# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from math import log


def main():
    n = int(input())
    if 17 <= n <= pow(10, 9):
        print('{:.1f} {:.1f}'.format(n / log(n), (n / log(n)) * 1.25506))


if __name__ == '__main__':
    main()
