# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    while True:
        try:
            n, m = map(int, input().split())
            lista = sorted([int(input()) for a in range(n)])[::-1]
            for a in range(m):
                print(lista[int(input()) - 1])
        except EOFError:
            break


if __name__ == '__main__':
    main()
