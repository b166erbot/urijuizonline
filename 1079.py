# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    listas = []
    pesos = [2, 3, 5]
    for a in range(int(input())):
        listas.append([float(b) for b in input().split()])
    for a in listas:
        valor = sum([a[c] * pesos[c] for c in range(3)]) / 10
        print('{:.1f}'.format(valor))


if __name__ == '__main__':
    main()
