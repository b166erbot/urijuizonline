# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    operacao = input()
    matriz, recorte, recorte2 = [], [], []
    while len(matriz) < 144:
        v = [float(a) for a in input().split()]
        if len(v) <= 144 - len(matriz):
            matriz += v
        else:
            matriz += v[:144 - len(matriz)]
    for a in range(0, 144, 12):
        recorte.append(matriz[a: a+12])
    for a in range(1, 12):
        recorte2 += recorte[a][12-a:]
    if operacao == 'S':
        print('{:.1f}'.format(sum(recorte2)))
    elif operacao == 'M':
        print('{:.1f}'.format(sum(recorte2) / len(recorte2)))


if __name__ == '__main__':
    main()
