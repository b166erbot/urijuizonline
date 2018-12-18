# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

pi = 3.14159


def main():
    lista = input().split()
    a, b, c = [float(item) for item in lista]
    print('TRIANGULO: {:.3f}'.format((a * c) / 2))
    print('CIRCULO: {:.3f}'.format(pi * pow(c, 2)))
    print('TRAPEZIO: {:.3f}'.format(((a + b) * c) / 2))
    print('QUADRADO: {:.3f}'.format(b * b))
    print('RETANGULO: {:.3f}'.format(a * b))


main()
