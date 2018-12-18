# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    c = 6
    for a in range(1, 10, 2):
        c += 2
        for b in range(1, 4):
            print('I={} J={}'.format(a, c - b))


if __name__ == '__main__':
    main()
