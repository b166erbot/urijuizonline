# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    lista = [int(input()) for _ in range(int(input()))]
    numeros_ordenados = sorted(set(lista))
    numeros_quantidades = map(lambda x: (x, lista.count(x)), numeros_ordenados)
    for numero, quantidade in numeros_quantidades:
        print('{} aparece {} vez(es)'.format(numero, quantidade))


if __name__ == '__main__':
    main()
