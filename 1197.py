# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

from operator import mul


def main():
    try:
        while True:
            entrada = list(map(int, input().split()))
            print(mul(*entrada) * 2)
    except EOFError:
        pass


if __name__ == '__main__':
    main()
