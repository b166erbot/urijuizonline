# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    quantidade = int(input())
    while quantidade != 0:
        lista = list(map(int, input().split()))
        john = sum(lista)
        mary = abs(john - quantidade)
        print("Mary won {} times and John won {} times".format(mary, john))
        quantidade = int(input())


if __name__ == '__main__':
    main()
