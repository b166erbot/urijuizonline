# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    lista = []
    for a in range(10):
        valor = int(input())
        if valor <= 0:
            valor = 1
        lista.append(valor)
    for a in range(10):
        print('X[{}] = {}'.format(a, lista[a]))


if __name__ == '__main__':
    main()
