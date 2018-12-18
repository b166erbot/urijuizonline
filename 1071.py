# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    x, y = int(input()), int(input())
    soma = 0
    for a in range((y+1), x):
        if a % 2 == 1:
            soma += a
    print(soma)


if __name__ == '__main__':
    main()
