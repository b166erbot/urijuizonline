# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    vezes, posicao = map(int, input().split())
    nomes = []
    for _ in range(vezes):
        nomes.append(input())
    print(sorted(nomes)[posicao - 1])


if __name__ == '__main__':
    main()
