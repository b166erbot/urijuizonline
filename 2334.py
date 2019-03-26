# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    n = int(input())
    while n > -1:
        print(n-1 if n > 0 else n)
        n = int(input())


if __name__ == '__main__':
    main()
