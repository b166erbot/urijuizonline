# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    print('Valores de b:\n' + '-' * 13)
    for a, b in zip(range(1, 6), ['n', ' >20', '0>20', ' <20', '%<2']):
        print('{}) b = {:{}}'.format(a, 7, b))
    print('\nValores de d:\n' + '-' * 13)
    temp = zip(range(1, 10), ['.6f', '.0f', '.1f', '.2f', '', ' >20', '0>20',
                              ' <20', '%<5.2f'])
    for a, b in temp:
        print('{}) d = {:{}}'.format(a, 2.208, b))


if __name__ == '__main__':
    main()
