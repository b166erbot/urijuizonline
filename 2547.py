# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    while True:
        try:
            n = 0
            x, y, z = map(int, input().split())
            for a in range(x):
                if int(input()) in range(y, z + 1):
                    n += 1
            print(n)
        except EOFError:
            break


if __name__ == '__main__':
    main()
