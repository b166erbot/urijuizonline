# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    competidores, folhas, distribuir = map(int, input().split())
    print('S' if folhas // distribuir >= competidores else 'N')


if __name__ == '__main__':
    main()
