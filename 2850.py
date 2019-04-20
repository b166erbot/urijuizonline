# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


dici = {'esquerda': 'ingles', 'direita': 'frances', 'nenhuma': 'portugues',
        'as duas': 'caiu'}


def main():
    while True:
        try:
            print(dici[input()])
        except EOFError:
            break


if __name__ == '__main__':
    main()
