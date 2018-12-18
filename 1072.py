# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    dentro = fora = 0
    vezes = int(input())
    for a in range(vezes):
        if 10 <= int(input()) <= 20:
            dentro += 1
        else:
            fora += 1
    print('{} in\n{} out'.format(dentro, fora))


if __name__ == '__main__':
    main()
