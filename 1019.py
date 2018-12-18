# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    segundos = int(input())
    h = segundos / (60 * 60)
    m = segundos % (60 * 60) / 60
    s = segundos % 60
    print('{}:{}:{}'.format(int(h), int(m), int(s)))


main()
