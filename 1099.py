# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    impares = []
    for a in range(int(input())):
        entrada = [int(c) for c in input().split()]
        entrada.sort()
        if entrada[0] % 2 == 1:
            entrada[0] += 1
        soma = 0
        for b in range(*entrada):
            if b % 2 == 1:
                soma += b
        impares.append(soma)
    for a in impares:
        print(a)


if __name__ == '__main__':
    main()
