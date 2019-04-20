# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    print('-' * 39)
    print('|  decimal  |  octal  |  Hexadecimal  |')
    print('-' * 39)
    for a in range(16):
        print('|  {0: ^9}|{0: ^9o}|{0: ^15X}|'.format(a))
    print('-' * 39)


if __name__ == '__main__':
    main()
