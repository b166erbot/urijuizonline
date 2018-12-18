# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def verificar(x, y):
    if int(x) == x and y == 0:
        print('Eixo X')
        return True
    elif int(y) == y and x == 0:
        print('Eixo Y')
        return True
    return False


def main():
    x, y = [float(n) for n in input().split()]
    if not any([x, y]):
        print('Origem')
    elif x <= 0 and y > 0:
        if not verificar(x, y):
            print('Q2')
    elif x <= 0 and y <= 0:
        if not verificar(x, y):
            print('Q3')
    elif x > 0 and y > 0:
        if not verificar(x, y):
            print('Q1')
    elif x > 0 and y <= 0:
        if not verificar(x, y):
            print('Q4')


main()
