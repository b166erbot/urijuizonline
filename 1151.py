# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    valor = int(input())
    while not valor < 46:
        valor = int(input())
    n, n2 = 0, 1
    lista = [0, 1]
    for a in range(valor-2):
        n3 = n + n2
        lista.append(n3)
        n = n2
        n2 = n3
    print(*lista)


if __name__ == '__main__':
    main()
