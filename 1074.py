# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    n = int(input())
    lista = []
    pi = pn = ''
    for a in range(n):
        lista.append(int(input()))
    for a in lista:
        if a % 2 == 0:
            pi = 'EVEN'
        else:
            pi = 'ODD'
        if a < 0:
            pn = 'NEGATIVE'
        elif a > 0:
            pn = 'POSITIVE'
        else:
            print('NULL')
            continue
        print(pi, pn)


if __name__ == '__main__':
    main()
