# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    a, b, c = map(int, input().split())
    if abs(a - b) == abs(b - c) and a != b != c and max([a, b, c]) == c:
        print(':)')
    elif abs(a - b) == abs(b - c):
        print(':(')
    elif (a + c) / 2 >= b:
        print(':)')
    else:
        print(':(')


if __name__ == '__main__':
    main()
