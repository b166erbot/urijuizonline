# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    ordem = []
    while True:
        a, b = [int(c) for c in input().split()]
        if a == b:
            break
        elif a < b:
            ordem.append('Crescente')
        elif a > b:
            ordem.append('Decrescente')
    for a in ordem:
        print(a)


if __name__ == '__main__':
    main()
