# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    forma = 'A = {}, B = {}, C = {}'
    a, b, c = input(), input(), input()
    print(forma.format(a, b, c))
    print(forma.format(b, c, a))
    print(forma.format(c, a, b))


if __name__ == '__main__':
    main()
