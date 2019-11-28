# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    lista = [1 if int(input()) > 1 else 0 for _ in range(int(input()))]
    print(sum(lista))


if __name__ == '__main__':
    main()
