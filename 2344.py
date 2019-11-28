# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    valor = int(input())
    dicio = {
        (0,): 'E',
        range(1, 36): 'D',
        range(36, 61): 'C',
        range(61, 86): 'B',
        range(86, 101): 'A'
    }
    for x in dicio:
        if valor in x:
            print(dicio[x])


if __name__ == '__main__':
    main()
