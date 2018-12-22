# -*- coding: utf-8 -*-


'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    soma = 0
    x, y = int(input()), int(input())
    if x > y:
        x, y = y, x
    for a in range(x, y + 1):
        if a % 13 != 0:
            soma += a
    print(soma)


if __name__ == '__main__':
    main()
