# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    valor = int(input())
    while valor != 0:
        print(*list(range(1, valor+1)))
        valor = int(input())


if __name__ == '__main__':
    main()
