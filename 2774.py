# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    while True:
        try:
            m, h = map(int, input().split())
            lista = [float(a) for a in input().split()]
            media = sum(lista) / len(lista)
            temp = (sum([(a - media) ** 2 for a in lista]) / (len(lista) - 1)) ** 0.5
            print('{:.5f}'.format(temp))
        except EOFError:
            break


if __name__ == '__main__':
    main()
