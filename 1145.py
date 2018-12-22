# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    x, y = [int(a) for a in input().split()]
    if 1 < x < 20 and x < y < 100000:
        for a in range(1, y + 1, x):
            linha = []
            for b in range(x):
                if a + b <= y:
                    linha.append(str(a+b))
            print(' '.join(linha))


if __name__ == '__main__':
    main()
