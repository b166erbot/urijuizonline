# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from operator import xor


def main():
    while True:
        try:
            print(xor(*[int(a) for a in input().split()]))
        except EOFError:
            break


if __name__ == '__main__':
    main()
