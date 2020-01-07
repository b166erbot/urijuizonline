# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    tamanho = int(input())
    dimensões = map(int, input().split())
    print('S' if all(map(lambda x: x >= tamanho, dimensões)) else 'N')


if __name__ == '__main__':
    main()
