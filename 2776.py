# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    while True:
        try:
            n, m = map(int, input().split())
            for a in range(n):
                q, v = map(int, input().split())
                
        except EOFError:
            break


if __name__ == '__main__':
    main()
