# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def validacao(n):
    return 1 <= n <= 1000


def mdc_recursivo(n, n2):
    resto = n % n2
    if not resto:
        return n2
    return mdc_recursivo(n2, resto)


def main():
    n = int(input())
    if not 1 <= n <= (1 * pow(10, 4)):
        return
    li = []
    for a in range(n):
        lista = input().split()
        temp = [int(a) for a in lista if a.isnumeric()]
        if not all([validacao(b) for b in temp]):
            return
        n1, d1, n2, d2 = temp
        sinal = lista[3]
        if sinal == '+':
            nl = [n1 * d2 + n2 * d1, d1*d2]
            mdc = int(mdc_recursivo(max(nl), min(nl)))
        elif sinal == '-':
            nl = [n1 * d2 - n2 * d1, d1 * d2]
            mdc = abs(int(mdc_recursivo(max(nl), min(nl))))
        elif sinal == '*':
            nl = [n1 * n2, d1 * d2]
            mdc = int(mdc_recursivo(max(nl), min(nl)))
        elif sinal == '/':
            nl = [n1 * d2, n2 * d1]
            mdc = int(mdc_recursivo(max(nl), min(nl)))
        li += ['{}/{} = {}/{}'.format(nl[0], nl[1], nl[0]//mdc, nl[1]//mdc)]
    for a in li:
        print(a)


main()
