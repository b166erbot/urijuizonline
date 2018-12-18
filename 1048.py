# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    salario = float(input())
    if 0 <= salario <= 400:
        reajuste = (salario // 100) * 15
        percentual = 15
    elif 400 < salario <= 800:
        reajuste = (salario // 100) * 12
        percentual = 12
    elif 800 < salario <= 1200:
        reajuste = (salario // 100) * 10
        percentual = 10
    elif 1200 < salario <= 2000:
        reajuste = (salario // 100) * 7
        percentual = 7
    elif salario > 2000:
        reajuste = (salario // 100) * 4
        percentual = 4
    print('Novo salario: {:.2f}'.format(salario + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: {} %'.format(percentual))


if __name__ == '__main__':
    main()
