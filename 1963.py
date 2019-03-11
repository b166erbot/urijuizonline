# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    vi, vf = map(float, input().split())
    print('{:.2f}'.format(abs(100 - (vf * 100) / vi)) + '%')


if __name__ == '__main__':
    main()
