# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    nome = input()
    salario = float(input())
    vendas = float(input())
    acrescimo = (vendas/100) * 15
    print('TOTAL = R$ {:.2f}'.format(salario + acrescimo))


main()
