# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    entrada = list(map(int, input().split()))
    entrada2 = list(map(int, input().split()))
    if entrada2 == list(map(lambda x: not x, entrada)):
        print('Y')
    else:
        print('N')


if __name__ == '__main__':
    main()
