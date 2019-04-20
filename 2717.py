# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    minutos = float(input())
    if sum(map(int, input().split())) <= minutos:
        print('Farei hoje!')
    else:
        print('Deixa para amanha!')


if __name__ == '__main__':
    main()
