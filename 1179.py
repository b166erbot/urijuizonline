# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    impares, pares = [], []
    for a in range(15):
        valor = int(input())
        if valor % 2 == 0:
            pares.append(valor)
        else:
            impares.append(valor)
        if len(pares) == 5:
            for b in range(5):
                print('par[{}] = {}'.format(b, pares[b]))
            pares.clear()
        elif len(impares) == 5:
            for b in range(5):
                print('impar[{}] = {}'.format(b, impares[b]))
            impares.clear()
    for a in range(len(impares)):
        print('impar[{}] = {}'.format(a, impares[a]))
    for a in range(len(pares)):
        print('par[{}] = {}'.format(a, pares[a]))


if __name__ == '__main__':
    main()
