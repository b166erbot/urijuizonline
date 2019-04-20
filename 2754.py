# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    a, b = 234.345, 45.698
    for x in ['.6f', '.0f', '.01f', '.02f', '.03f', 'e', 'E', '', '']:
        print('{0:{2}} - {1:{2}}'.format(a, b, x))


if __name__ == '__main__':
    main()
