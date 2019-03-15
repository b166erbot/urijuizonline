# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    dicionario = {1001: 1.50, 1002: 2.50, 1003: 3.50,
                  1004: 4.50, 1005: 5.50}
    valor = 0
    for a in range(int(input())):
        item, quantidade = map(int, input().split())
        valor += dicionario[item] * quantidade
    print('{:.2f}'.format(valor))


if __name__ == '__main__':
    main()
