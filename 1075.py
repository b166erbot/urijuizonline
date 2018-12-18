# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    n = int(input())
    if not n < 10000:
        return
    for a in range(1, 10001):
        if a % n == 2:
            print(a)


if __name__ == '__main__':
    main()
