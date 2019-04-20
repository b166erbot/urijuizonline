# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    d, m, a = input().split('/')
    print('{}/{}/{}'.format(m, d, a))
    print('{}/{}/{}'.format(a, m, d))
    print('{}-{}-{}'.format(d, m, a))


if __name__ == '__main__':
    main()
