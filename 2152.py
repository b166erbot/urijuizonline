# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    for a in range(int(input())):
        h, m, abriu = map(int, input().split())
        p = 'abriu' if abriu else 'fechou'
        print('{:0>2d}:{:0>2d} - A porta {}!'.format(h, m, p))


if __name__ == '__main__':
    main()
