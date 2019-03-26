# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    x, y = map(int, input().split())
    while (x, y) != (0, 0):
        print(x * y)
        x, y = map(int, input().split())


if __name__ == '__main__':
    main()
