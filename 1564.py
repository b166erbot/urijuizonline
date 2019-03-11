# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    try:
        while True:
            n = int(input())
            if n > 0:
                print('vai ter duas!')
            else:
                print('vai ter copa!')
    except EOFError:
        pass


if __name__ == '__main__':
    main()
