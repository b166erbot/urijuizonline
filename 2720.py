# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def t(x):
    return sum([int(a) for a in x[1:]])


def main():
    for a in range(int(input())):
        n, k = map(int, input().split())
        dici = [input().split() for a in range(n)]
        temp = [dici.pop(dici.index(max(dici, key=t)))[0] for a in range(k)]
        print(*sorted(temp))


if __name__ == '__main__':
    main()
