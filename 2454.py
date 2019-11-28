# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def fluxo(x, y):
    if not x:
        return 'C'
    else:
        if y:
            return 'A'
        else:
            return 'B'


def main():
    x, y = list(map(int, input().split()))
    print(fluxo(x, y))


if __name__ == '__main__':
    main()
