# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    input()
    # o python nao necessita da primeira entrada, portanto, sera descartada.
    numeros = list(map(int, input().split()))
    for a in [2, 3, 4, 5]:
        m = len(list(filter(lambda x: x % a == 0, numeros)))
        print('{} Multiplo(s) de {}'.format(m, a))


if __name__ == '__main__':
    main()
