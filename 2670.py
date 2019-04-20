# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    a = [int(input()) for a in range(3)]
    cenarios = [a[0] * 4 + a[1] * 2, a[2] * 4 + a[1] * 2, (a[0] + a[2]) * 2]
    print(min(cenarios))


if __name__ == '__main__':
    main()
