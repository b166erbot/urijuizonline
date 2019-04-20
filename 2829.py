# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    lista = [input() for a in range(int(input()))]
    lista = sorted(lista, key=lambda x: (x.lower(), x))
    print(*lista, sep='\n')


if __name__ == '__main__':
    main()
