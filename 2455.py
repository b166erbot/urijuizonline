# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    a, b, c, d = list(map(int, input().split()))
    pessoa1, pessoa2 = a * b, c * d
    if pessoa1 == pessoa2:
        print(0)
    elif pessoa1 < pessoa2:
        print(1)
    elif pessoa1 > pessoa2:
        print(-1)


if __name__ == '__main__':
    main()
