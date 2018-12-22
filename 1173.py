# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    valor = int(input())
    lista = [valor]
    if valor <= 50:
        for a in range(10):
            print('N[{}] = {}'.format(a, lista[-1]))
            lista.append(lista[-1]*2)


if __name__ == '__main__':
    main()
