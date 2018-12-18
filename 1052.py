# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    meses = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
             'August', 'September', 'October', 'November', 'December']
    meses = dict(zip(list(range(1, 13)), meses))
    valor = int(input())
    if 0 < valor <= 12:
        print(meses[valor])


if __name__ == '__main__':
    main()
