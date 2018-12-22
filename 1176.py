# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def fibonacci(numero):
    x, y = 0, 1
    lista = [0, 1]
    for a in range(numero):
        x, y = y, x+y
        lista.append(y)
    return lista


def main():
    lista = fibonacci(60)
    n = int(input())
    for a in range(n):
        valor = int(input())
        if 0 <= valor <= 60:
            print('Fib({}) = {}'.format(valor, lista[valor]))


if __name__ == '__main__':
    main()
