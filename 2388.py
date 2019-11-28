# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


from operator import mul


def main():
    vezes = range(int(input()))
    itens = [mul(*map(int, input().split())) for _ in vezes]
    print(sum(itens))


if __name__ == '__main__':
    main()
