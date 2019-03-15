# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    while True:
        try:
            v = float(input())
            d = float(input())
        except EOFError:
            break
        area = 3.14 * pow(d/2, 2)
        print('ALTURA = {:.2f}'.format(v/area))
        print('AREA = {:.2f}'.format(area))


if __name__ == '__main__':
    main()
