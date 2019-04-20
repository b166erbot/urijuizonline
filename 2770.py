# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    while True:
        try:
            x, y, m = map(int, input().split())
            for a in range(m):
                a, b = [int(a) for a in input().split()]
                if a <= x and b <= y or b <= x and a <= y:
                    print('Sim')
                else:
                    print('Nao')
        except EOFError:
            break


if __name__ == '__main__':
    main()
