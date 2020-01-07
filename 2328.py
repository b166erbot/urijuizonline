# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    lista = list(map(int, input().split()))
    n = lista[0]
    if len(lista) == 1:
        lista = list(map(int, input().split()))
    else:
        lista.pop(0)
    print(sum(lista) - n)


if __name__ == '__main__':
    main()
