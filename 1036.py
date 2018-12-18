# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def x(delta, a, b):
    x1 = (-b + delta**0.5) / (2 * a)
    x2 = (-b - delta**0.5) / (2 * a)
    return x1, x2


def main():
    lista = [float(a) for a in input().split()]
    if any([a <= 0 for a in lista]):
        return print('Impossivel calcular')
    a, b, c = lista
    delta = pow(b, 2) - 4 * a * c
    if delta > 0:
        x1, x2 = x(delta, a, b)
        print('R1 = {:.5f}\nR2 = {:.5f}'.format(x1, x2))
    else:
        print('Impossivel calcular')


main()
