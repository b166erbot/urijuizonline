# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from operator import mul


def main():
    while True:
        try:
            lista = []
            for a in range(int(input())):
                lista.append(list(map(int, input().split())))
            temp = sum(map(lambda x: mul(*x), lista))
            temp2 = sum([a[1] for a in lista]) * 100
            print('{:.4f}'.format(temp/temp2))
        except EOFError:
            break


if __name__ == '__main__':
    main()
