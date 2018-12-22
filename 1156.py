# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    x, y = 3, 2
    soma = 1
    while x < 39:
        soma += x/y
        x, y, = x+2, y*2
    print('{:.2f}'.format(soma))


if __name__ == '__main__':
    main()
