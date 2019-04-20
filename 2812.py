# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    for a in range(int(input())):
        saida = []
        input()
        lista = sorted([int(a) for a in input().split() if int(a) % 2 == 1])
        if lista:
            chave = False
            while lista:
                chave = not chave
                saida.append(str(lista.pop(-1 if chave else 0)))
        print(' '.join(saida))


if __name__ == '__main__':
    main()
