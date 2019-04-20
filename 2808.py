# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    a, c = (a.encode() for a in input().split())
    a, b = a
    c = list(c)
    condicoes = ([a-2, b-1] == c, [a-1, b-2] == c, [a+1, b-2] == c,
                 [a+2, b-1] == c, [a-2, b+1] == c, [a-1, b+2] == c,
                 [a+1, b+2] == c, [a+2, b+1] == c)
    if any(condicoes):
        print('VALIDO')
    else:
        print('INVALIDO')


if __name__ == '__main__':
    main()
