# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def posi(n):
    return n > 0


def main():
    lista = []
    for a in range(6):
        entrada = float(input())
        if posi(entrada):
            lista.append(entrada)
    if not lista:
        return
    print('{} valores positivos'.format(len(lista)))
    print('{:.1f}'.format(sum(lista) / len(lista)))


if __name__ == '__main__':
    main()
