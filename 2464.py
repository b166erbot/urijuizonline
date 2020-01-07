# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    troca = input()
    frase = input()
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    dicionario = {x: y for x, y in zip(alfabeto, troca)}
    print(''.join(map(lambda x: dicionario[x], frase)))


if __name__ == '__main__':
    main()
