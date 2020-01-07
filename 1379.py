# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    a, b = map(int, input().split())
    while (a, b) != (0, 0):
        c = a - abs(a - b)
        print(c)
        a, b = map(int, input().split())


if __name__ == '__main__':
    main()
