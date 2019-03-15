# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def verificar_matriz(matriz):
    retornar = [''] * (len(matriz) - 1)
    for a in range(len(matriz) - 1):
        for b in range(len(matriz[0]) - 1):
            tmp = matriz[a][b: b+2] + matriz[a+1][b: b+2]
            if sum(tmp) >= 2:
                retornar[a] += 'S'
            else:
                retornar[a] += 'U'
    return retornar


def main():
    n = []
    for a in range(int(input()) + 1):
        n.append(list(map(int, input().split())))
    print(*verificar_matriz(n), sep='\n')


if __name__ == '__main__':
    main()
