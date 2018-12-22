# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    soma = 0
    lista = [int(a) for a in input().split()]
    while len([a for a in lista[1:] if a > 0]) < 1:
        lista = [int(a) for a in input().split()]
    x, y = lista[0], [a for a in lista[1:] if a > 0][0]
    for a in range(y):
        soma += x + a
    print(soma)


if __name__ == '__main__':
    main()
