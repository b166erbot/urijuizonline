# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from pdb import set_trace


def sortudo(x):
    set_trace()
    for a in range(1, len(x), 2):
        x.pop(a)
    for a in range(1, len(x), 3):
        x.pop(a)
    for a in range(1, len(x), 4):
        x.pop(a)
    return x


def main():
    input()
    lista = sortudo(input().split())
    print('Y' if input() in lista else 'N')


if __name__ == '__main__':
    main()
