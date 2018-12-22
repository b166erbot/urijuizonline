# -*- coding: utf-8 -*-
# eu poderia ter feito com listas mas por eu não querer utilizar 2 fore fazer da
# maneira certa, prefiro nem usar listas (ou qualquer outra builtin function)

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def menor_11(x):
    return True if x <= 10 else False


def main():
    for a in range(100):
        valor = float(input())
        if menor_11(valor):
            print('A[{}] = {}'.format(a, valor))


if __name__ == '__main__':
    main()
