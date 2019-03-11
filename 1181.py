# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    linha = int(input())
    operacao = input()
    matrix, matrix2 = [], []
    if 0 <= linha <= 11:
        while len(matrix) < 144:
            v = [float(a) for a in input().split()]
            if len(v) <= 144 - len(matrix):
                matrix += v
            else:
                matrix += v[:144 - len(matrix)]
        for a in range(0, 144, 12):
            matrix2.append(matrix[a: a+12])
        if operacao == 'S':
            print('{:.1f}'.format(sum(matrix2[linha])))
        elif operacao == 'M':
            print('{:.1f}'.format(sum(matrix2[linha]) / 12))


if __name__ == '__main__':
    main()
