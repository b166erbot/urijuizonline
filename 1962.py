# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    for a in range(int(input())):
        ano = 2015 - int(input())
        if ano > 0:
            print('{} D.C.'.format(ano))
        else:
            print('{} A.C.'.format(abs(ano)+1))


if __name__ == '__main__':
    main()
