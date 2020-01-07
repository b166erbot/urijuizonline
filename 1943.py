# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

from itertools import dropwhile


def main():
    top = [1, 3, 5, 10, 25, 50, 100]
    entrada = int(input())
    numero = next(dropwhile(lambda x: x < entrada, top))
    print('Top {}'.format(numero))


if __name__ == '__main__':
    main()
