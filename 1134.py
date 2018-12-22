# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    lista = [0, 0, 0]
    while True:
        codigo = int(input())
        while codigo not in [1, 2, 3, 4]:
            codigo = int(input())
        if codigo == 4:
            break
        else:
            lista[codigo-1] += 1
    print('MUITO OBRIGADO')
    print('Alcool: {}'.format(lista[0]))
    print('Gasolina: {}'.format(lista[1]))
    print('Diesel: {}'.format(lista[2]))


if __name__ == '__main__':
    main()
