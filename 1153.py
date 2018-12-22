# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def fatorial(x):
    if x == 1:
        return x
    return fatorial(x-1) * x


def main():
    valor = int(input())
    while not 0 < valor < 13:
        valor = int(input())
    print(fatorial(valor))


if __name__ == '__main__':
    main()
