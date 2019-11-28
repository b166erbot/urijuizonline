# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    cv, ce, cs, fv, fe, fs = map(int, input().split())
    c_pontos = cv * 3 + ce
    f_pontos = fv * 3 + fe
    if c_pontos == f_pontos:
        if cs > fs:
            print('C')
        elif fs > cs:
            print('F')
        else:
            print('=')
    elif c_pontos > f_pontos:
        print('C')
    elif f_pontos > c_pontos:
        print('F')


if __name__ == '__main__':
    main()
