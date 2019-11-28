# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    n = int(input())
    x, y = map(int, input().split())
    lavadoura = range(x, y + 1)
    x, y = map(int, input().split())
    secadoura = range(x, y + 1)
    if all([n in lavadoura, n in secadoura]):
        print('possivel')
    else:
        print('impossivel')


if __name__ == '__main__':
    main()
