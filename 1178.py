# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    valor = float(input())
    divisor = 2
    print('N[{}] = {:.4f}'.format(0, valor))
    for a in range(1, 100):
        print('N[{}] = {:.4f}'.format(a, valor/divisor))
        divisor *= 2


if __name__ == '__main__':
    main()
