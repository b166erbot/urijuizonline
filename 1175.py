# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    lista = []
    for a in range(20):
        valor = int(input())
        lista.append(valor)
    lista = lista[::-1]
    for a in range(20):
        print('N[{}] = {}'.format(a, lista[a]))


if __name__ == '__main__':
    main()
