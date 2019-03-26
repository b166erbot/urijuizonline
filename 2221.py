# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    for a in range(int(input())):
        bonus = int(input())
        bonus2 = bonus
        a, d, l = map(int, input().split())  # noqa
        a2, d2, l2 = map(int, input().split())
        bonus = 0 if l % 2 else bonus
        bonus2 = 0 if l2 % 2 else bonus2
        if (a + d) / 2 + bonus > (a2 + d2) / 2 + bonus2:
            print('Dabriel')
        elif (a + d) / 2 + bonus < (a2 + d2) / 2 + bonus2:
            print('Guarte')
        else:
            print('Empate')


if __name__ == '__main__':
    main()
