# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    soma = 1
    for a in range(2, 101):
        soma += 1/a
    print('{:.2f}'.format(soma))


if __name__ == '__main__':
    main()
