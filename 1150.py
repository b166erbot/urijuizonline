# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    x, z = int(input()), int(input())
    while z <= x:
        z = int(input())
    contagem = 0
    w = x
    while x < z:
        contagem += 1
        x += w + contagem
    print(contagem + 1)


if __name__ == '__main__':
    main()
