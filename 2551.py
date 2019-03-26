# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from operator import truediv


def main():
    while True:
        try:
            maior = 0
            for a in range(1, int(input())+1):
                entrada = truediv(*map(int, input().split()[::-1]))
                if maior < entrada:
                    maior = entrada
                    print(a)
        except EOFError:
            break


if __name__ == '__main__':
    main()
