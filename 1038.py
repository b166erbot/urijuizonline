# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    dicionario = {1: 4.0, 2: 4.50, 3: 5.0, 4: 2.0, 5: 1.50}
    item, quantidade= [int(a) for a in input().split()]
    print('Total: R$ {:.2f}'.format(dicionario[item] * quantidade))


main()
