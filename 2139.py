# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from datetime import date


def main():
    natal = date(2016, 12, 25)
    lista = []
    while True:
        try:
            lista.append(list(map(int, input().split())))
        except EOFError:
            break
    for a, b in lista:
        atual = date(2016, a, b)
        dias = (natal - atual).days
        if dias == 1:
            print('E vespera de natal!')
        elif dias == 0:
            print('E natal!')
        elif dias < 1:
            print('Ja passou!')
        else:
            print('Faltam {} dias para o natal!'.format(dias))


if __name__ == '__main__':
    main()
