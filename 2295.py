# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def regra_3(x, y, z):
    return z * y / x


def main():
    a, g, ar, gr = map(float, input().split())
    ar2 = regra_3(a, ar, g)
    print('A' if ar2 > gr else 'G')


if __name__ == '__main__':
    main()
