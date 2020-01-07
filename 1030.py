# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

import sys
sys.setrecursionlimit(100000)


def josephus(n, k):
    if n == 1:
        return 1
    return (josephus(n - 1, k) + k-1) % n + 1


def main():
    for x in range(1, int(input()) + 1):
        n, k = map(int, input().split())
        print('Case {}: {}'.format(x, josephus(n, k)))


if __name__ == '__main__':
    main()
