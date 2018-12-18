# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    n = int(input())
    if not 5 < n < 2000:
        return
    for a in range(2, n + 1, 2):
        print('{}^2 = {}'.format(a, a**2))


if __name__ == '__main__':
    main()
