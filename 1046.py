# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    hi, hf = [int(a) for a in input().split()]
    if hi >= hf:
        print('O JOGO DUROU {} HORA(S)'.format(abs(hi - 24) + hf))
    else:
        print('O JOGO DUROU {} HORA(S)'.format(abs(2 - 16)))


main()
