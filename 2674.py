# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def ePrimo(x):
    if x == 2:
        return True
    elif x in [0, 1, 4, 6, 8]:
        return False
    else:
        return sum([x / a == x // a for a in range(3, x, 2)]) == 0


def main():
    lista = []
    while True:
        try:
            lista += input().split()
        except EOFError:
            break
    for b in lista:
        if ePrimo(int(b)):
            if all([ePrimo(int(a)) for a in b]):
                print('Super')
            else:
                print('Primo')
        else:
            print('Nada')


if __name__ == '__main__':
    main()
