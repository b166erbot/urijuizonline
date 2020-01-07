# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    vezes, saldo = map(int, input().split())
    menor_saldo = saldo
    for _ in range(vezes):
        saldo += int(input())
        if saldo < menor_saldo:
            menor_saldo = saldo
    print(menor_saldo)


if __name__ == '__main__':
    main()
