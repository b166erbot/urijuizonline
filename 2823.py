# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from operator import truediv


def main():
    final = 0
    for a in range(int(input())):
        final += truediv(*[int(a) for a in input().split()])
    print('OK' if final <= 1 else 'FAIL')


if __name__ == '__main__':
    main()
