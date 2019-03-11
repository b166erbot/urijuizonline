# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from decimal import Decimal


def main():
    alunos_notas = dict()
    for a in range(int(input())):
        b, c = input().split()
        b, c = int(b), Decimal(c)
        alunos_notas[c] = b
    if any(map(lambda x: x >= 8, alunos_notas)):
        print(alunos_notas[max(alunos_notas)])
    else:
        print('Minimum note not reached')


if __name__ == '__main__':
    main()
