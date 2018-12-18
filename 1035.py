# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    a, b, c, d = [int(a) for a in input().split()]
    condicoes = [b > c, d > a, (c + d) > (a + b),
                 c > 0 < d, a % 2 == 0]
    if all(condicoes):
        print('Valores aceitos')
    else:
        print('Valores nao aceitos')


main()
