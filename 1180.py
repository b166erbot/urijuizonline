# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    n = int(input())
    valores = []
    if 1 <= n <= 1000:
        while len(valores) < n:
            v = [int(a) for a in input().split()]
            if len(v) <= n - len(valores):
                valores += v
            else:
                valores += v[:n - len(valores)]
        print('Menor valor: {}'.format(min(valores)))
        print('Posicao: {}'.format(valores.index(min(valores))))


if __name__ == '__main__':
    main()
