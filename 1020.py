# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    dias = int(input())
    a = dias // 365
    dias = dias % 365
    m = dias // 30
    dias = dias % 30
    d = int(dias)
    print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(a, m, d))


main()
