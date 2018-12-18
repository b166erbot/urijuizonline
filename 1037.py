# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    intervalos = [[0, 25], [25, 50], [50, 75], [75, 100]]
    valor = float(input())
    if 0 <= valor <= 25.000000:
        print('Intervalo [0,25]')
    elif 25.000000 < valor <= 50.0000000:
        print('Intervalo (25,50]')
    elif 50.0000000 < valor <= 75.0000000:
        print('Intervalo (50,75]')
    elif 75.0000000 < valor <= 100.0000000:
        print('Intervalo (75,100]')
    else:
        print('Fora de intervalo')


main()
