# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def diferenca(x, y):
    return abs(x - y)


def main():
    input()
    lista = [int(a) for a in input().split()]
    if len(lista) == 1:
        return print(1)
    lista = [(lista[a], lista[a+1]) for a in range(len(lista) - 1)]
    final = 1
    dif = diferenca(*lista.pop(0))
    for a in lista:
        if diferenca(*a) != dif:
            final += 1
        dif = diferenca(*a)
    print(final)


if __name__ == '__main__':
    main()
