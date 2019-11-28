# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    abertura = int(input())
    vezes = range(int(input()))
    lista = [1 if abertura * int(input()) >= 40000000 else 0 for _ in vezes]
    print(sum(lista))


if __name__ == '__main__':
    main()
