# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    n = int(input())
    m = int(input())
    if n % 2 == 0 and m % 2 == 1:
        print(0)
    elif n % 2 == 1 and m % 2 == 0:
        print(0)
    else:
        print(1)


if __name__ == '__main__':
    main()
