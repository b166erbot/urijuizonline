# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    valores = input().split()
    valores = [int(a) for a in valores]
    print('{} eh o maior'.format(max(valores)))


main()
