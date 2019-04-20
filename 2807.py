# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def fibonacci(x):
    lista = [1, 2]
    if x == 1:
        return 1
    elif x == 2:
        return '1 1'
    while x-3 > 0:
        lista.append(sum(lista[-2:]))
        x -= 1
    return ' '.join([str(a) for a in lista[::-1]]) + ' 1'


def main():
    print(fibonacci(int(input())))


if __name__ == '__main__':
    main()
