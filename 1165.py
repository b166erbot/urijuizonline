# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    n = int(input())
    if 1 <= n <= 100:
        for a in range(n):
            valor = int(input())
            if 1 <= valor <= pow(10, 7):
                divisoes = 0
                for a in range(1, valor + 1):
                    if valor / a == valor // a:
                        divisoes += 1
                if divisoes == 2:
                    print('{} eh primo'.format(valor))
                else:
                    print('{} nao eh primo'.format(valor))


if __name__ == '__main__':
    main()
