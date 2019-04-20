# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    while True:
        valor = float('inf')
        try:
            for a in range(int(input())):
                t = float(input())
                valor = t if t < valor else valor
        except EOFError:
            break
        print(valor)


if __name__ == '__main__':
    main()
