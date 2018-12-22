# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    for a in range(int(input())):
        x, y = [int(b) for b in input().split()]
        if y == 0:
            print('divisao impossivel')
        else:
            print(x / y)


if __name__ == '__main__':
    main()
