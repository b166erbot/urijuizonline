# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from operator import truediv


def main():
    print('{:.2f}'.format(float(truediv(*map(int, input().split())))))


if __name__ == '__main__':
    main()
