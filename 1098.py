# -*- coding: utf-8 -*-
from decimal import Decimal

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    i, j = 0, 1
    while i <= 2:
        print('I={} J={}'.format(i, j))
        j += 1
        if j == (i + 4):
            i += Decimal('0.2')
            j -= Decimal('2.8')

if __name__ == '__main__':
    main()
