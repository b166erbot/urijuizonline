# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    lista = []
    while True:
        try:
            lista.append(int(input()) - 1)
        except EOFError:
            break
    print(*lista, sep='\n')


if __name__ == '__main__':
    main()
