# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    disponiveis = list(map(int, input().split()))
    pedidos = list(map(int, input().split()))
    soma = 0
    for a, b in zip(disponiveis, pedidos):
        t = a - b
        if t < 0:
            soma += abs(t)
    print(soma)


if __name__ == '__main__':
    main()
