# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    while True:
        try:
            entrada = input()
            input()  # o python nao necessita dessa entrada
            itens = map(int, input().split())
            print(''.join([entrada[a-1] for a in itens]))
        except:
            break


if __name__ == '__main__':
    main()
