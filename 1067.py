# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    valor = int(input())
    if not 0 < valor <= 1000:
        return
    for a in range(1, valor + 1, 2):
        print(a)


if __name__ == '__main__':
    main()
