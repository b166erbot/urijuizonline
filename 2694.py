# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

from re import findall


def main():
    for _ in range(int(input())):
        numeros = findall(r"\d+", input())
        soma = sum(map(int, numeros))
        print(soma)


if __name__ == '__main__':
    main()
