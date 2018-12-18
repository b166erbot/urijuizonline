# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    valor = int(input())
    if valor % 2 == 0:
        valor += 1
    for a in range(6):
        print(a * 2 + valor)


if __name__ == '__main__':
    main()
