# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    lista = set()
    n = int(input())
    for a in range(int(input())):
        lista.add(input())
    print(abs(n - len(lista)))


if __name__ == '__main__':
    main()
