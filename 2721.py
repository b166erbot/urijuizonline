# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    lista = ['Rudolph', 'Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet',
             'Cupid', 'Donner', 'Blitzen']
    print(lista[sum(map(int, input().split())) % 9])


if __name__ == '__main__':
    main()
