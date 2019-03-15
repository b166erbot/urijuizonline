# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    t = int(input())
    while t:
        for a in range(t):
            entrada = int(input())
            if entrada % 2 == 0:
                print(2 * entrada - 2)
            else:
                print(2 * entrada - 1)
        t = int(input())


if __name__ == '__main__':
    main()
