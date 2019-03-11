# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from itertools import permutations, combinations  # noqa


def triangulo(x):
    return all(map(lambda x: x[0] + x[1] > x[2], permutations(x)))


def main():
    a, b, c, d = map(int, input().split())
    if any(list(map(triangulo, combinations([a, b, c, d], 3)))):
        print('S')
    else:
        print('N')


if __name__ == '__main__':
    main()
