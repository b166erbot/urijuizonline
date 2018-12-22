# -*- coding: utf-8 -*-


'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    x, y = int(input()), int(input())
    if x > y:
        x, y = y, x
    for a in range(x + 1, y):
        if a % 5 in [2, 3]:
            print(a)


if __name__ == '__main__':
    main()
