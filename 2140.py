# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from itertools import permutations


def main():
    notas = [2, 5, 10, 20, 50, 100]
    n, m = map(int, input().split())
    while not n == m == 0:
        r = abs(n - m)
        if any(map(lambda x: r - sum(x) == 0, permutations(notas, 2))):
            print('possible')
        else:
            print('impossible')
        n, m = map(int, input().split())


if __name__ == '__main__':
    main()
