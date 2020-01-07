# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def calcular(x, y):
    return x // 3 * (y // 3)


def main():
    for _ in range(int(input())):
        medidas = map(int, input().split())
        print(calcular(*medidas))


if __name__ == '__main__':
    main()
