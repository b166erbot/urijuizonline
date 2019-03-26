# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    while True:
        try:
            input()  # python nao precisa dessa input
            lista = list(map(int, input().split()))
            if sum(lista) >= (len(lista) * 2) / 3:
                print('impeachment')
            else:
                print('acusacao arquivada')
        except EOFError:
            break


if __name__ == '__main__':
    main()
