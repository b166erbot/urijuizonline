# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    valor = int(input())
    while valor != 0:
        if valor % 2 == 1:
            valor += 1
        soma = 0
        for a in range(valor, valor+10, 2):
            soma += a
        valor = int(input())
        print(soma)


if __name__ == '__main__':
    main()
