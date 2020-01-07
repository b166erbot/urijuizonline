# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def magia(lista):
    return int(lista[0]), int(lista[2])


def main():
    operadores = {'+': lambda x, y: x + y, '*': lambda x, y: x * y}
    maximo = int(input())
    entrada = input().split()
    x, y = magia(entrada)
    funcao = operadores[entrada[1]]
    resultado = funcao(x, y)
    print('OK' if resultado <= maximo else 'OVERFLOW')


if __name__ == '__main__':
    main()
