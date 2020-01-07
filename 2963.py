# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    vezes = range(int(input()))
    numeros = [int(input()) for _ in vezes]
    primeiro = numeros[0]
    eleito = all(map(lambda x: x <= primeiro, numeros))
    print('S' if eleito else 'N')


if __name__ == '__main__':
    main()
