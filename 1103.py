# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

from datetime import datetime


def datetime_arrumado(lista):
    x, y = lista
    return datetime(1, 1, 1, x, y, 0, 0)


def main():
    entrada = list(map(int, input().split()))
    while entrada != [0, 0, 0, 0]:
        inicio = datetime_arrumado(entrada[:2])
        final = datetime_arrumado(entrada[2:])
        resultado = (final - inicio).seconds // 60
        print(resultado or 1440)
        entrada = list(map(int, input().split()))


if __name__ == '__main__':
    main()
