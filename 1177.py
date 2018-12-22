# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    valor = int(input())
    if 2 <= valor <= 50:
        lista = list(range(valor))
        for a in range(1000):
            print('N[{}] = {}'.format(a, lista[a % valor]))


if __name__ == '__main__':
    main()
