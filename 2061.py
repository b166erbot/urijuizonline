# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    n, m = map(int, input().split())
    lista = []
    for a in range(m):
        lista.append(input())
    n += lista.count('fechou')
    n -= lista.count('clicou')
    print(n)


if __name__ == '__main__':
    main()
