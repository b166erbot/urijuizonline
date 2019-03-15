# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def verificar_submatriz(matriz, n, m):
    submatriz = [[7, 7, 7], [7, 42, 7], [7, 7, 7]]
    for a in range(n-2):
        for b in range(m-2):
            tmp = [matriz[a][b: b+3], matriz[a+1][b: b+3], matriz[a+2][b: b+3]]
            if tmp == submatriz:
                return a+2, b+2
    return 0, 0


def main():
    matriz = []
    n, m = map(int, input().split())
    for a in range(n):
        matriz.append(list(map(int, input().split())))
    print(*verificar_submatriz(matriz, n, m))


if __name__ == '__main__':
    main()
