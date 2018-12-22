# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    for a in range(int(input())):
        soma = 0
        x, y = [int(b) for b in input().split()]
        if x % 2 == 0:
            x += 1
        for b in range(y):
            soma += x
            x += 2
        print(soma)


if __name__ == '__main__':
    main()
