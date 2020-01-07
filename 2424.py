# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    x, y = map(int, input().split())
    if all((x in range(433), y in range(469))):
        print('dentro')
    else:
        print('fora')


if __name__ == '__main__':
    main()
