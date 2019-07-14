# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    a, b = map(int, input().split())
    case = 0
    while a > 0 < b:
        lista = []
        procuras = []
        for c in range(a):
            lista.append(input())
        for c in range(b):
            procuras.append(input())
        case += 1
        print('CASE# {}:'.format(case))
        lista.sort()
        for a in range(len(procuras)):
            if procuras[a] in lista:
                print('{} found at {}'.format(procuras[a],
                                              lista.index(procuras[a]) + 1))
            else:
                print('{} not found'.format(procuras[a]))
        a, b = map(int, input().split())


if __name__ == '__main__':
    main()
