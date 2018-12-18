# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    lista = []
    for a in range(100):
        valor = int(input())
        lista.append(valor)
    print(max(lista))
    print(lista.index(max(lista)) + 1)


if __name__ == '__main__':
    main()
