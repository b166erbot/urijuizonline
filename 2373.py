# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    derrubados = 0
    for _ in range(int(input())):
        l, c = map(int, input().split())
        if l > c:
            derrubados += c
    print(derrubados)


if __name__ == '__main__':
    main()
