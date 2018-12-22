# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    while True:
        x, y = [int(a) for a in input().split()]
        if x > 0 and y > 0:
            print('primeiro')
        elif x > 0 and y < 0:
            print('quarto')
        elif x < 0 and y < 0:
            print('terceiro')
        elif x < 0 and y > 0:
            print('segundo')
        else:
            break


if __name__ == '__main__':
    main()
