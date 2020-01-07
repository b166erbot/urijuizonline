# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    for _ in range(int(input())):
        inicio, final = map(int, input().split())
        numeros = ''.join(map(str, range(inicio, final + 1)))
        print(numeros + numeros[::-1])


if __name__ == '__main__':
    main()
