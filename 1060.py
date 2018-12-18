# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    positivos = 0
    for a in range(6):
        if float(input()) > 0:
            positivos += 1
    print('{} valores positivos'.format(positivos))


if __name__ == '__main__':
    main()
