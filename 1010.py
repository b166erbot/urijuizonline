# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def mult(valor, valor2):
    return int(valor) * float(valor2)


def main():
    lista = input().split()
    lista2 = input().split()
    calculo = mult(*lista[1:]) + mult(*lista2[1:])
    print('VALOR A PAGAR: R$ {:.2f}'.format(calculo))


main()
