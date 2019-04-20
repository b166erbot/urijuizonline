# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    a, b, c = int(input()), int(input()), int(input())
    formula = 'A = {0:{3}}, B = {1:{4}}, C = {2:{5}}'
    print(formula.format(a, b, c, '', '', ''))
    print(formula.format(a, b, c, '> 10', '> 10', '> 10'))
    print(formula.format(a, b, c, '0=10d', '>010', '>010'))
    print(formula.format(a, b, c, '<10', '<10', '<10'))


if __name__ == '__main__':
    main()
