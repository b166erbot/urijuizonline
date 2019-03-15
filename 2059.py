# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    p, j1, j2, r, a = map(int, input().split())
    if r:
        if a:
            print('Jogador 2 ganha!')
        else:
            print('Jogador 1 ganha!')
    else:
        if a:
            print('Jogador 1 ganha!')
        else:
            # par ou impar normal
            if sum([j1, j2]) % 2 == (not p):
                print('Jogador 1 ganha!')
            else:
                print('Jogador 2 ganha!')


if __name__ == '__main__':
    main()
