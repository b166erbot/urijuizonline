# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    input()
    lista = {int(a) for a in input().split()}
    lista2 = {int(a) for a in input().split()}
    print(abs(len((lista & lista2)) - len(lista)))


if __name__ == '__main__':
    main()
