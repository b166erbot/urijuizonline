# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from math import sqrt


def main():
    while True:
        try:
            xf, yf, xi, yi, vi, r1, r2 = map(int, input().split())
            f = r1 + r2
            i = sqrt(pow(xf - xi, 2) + pow(yf - yi, 2)) + vi * 1.5
            if f >= i:
                print('Y')
            else:
                print('N')
        except EOFError:
            break


if __name__ == '__main__':
    main()
