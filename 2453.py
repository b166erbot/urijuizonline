# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def filter_impar(palavra):
    resultado = ''
    for index, caracter in enumerate(palavra):
        if index % 2 == 1:
            resultado += caracter
    return resultado


def main():
    entrada = input().split()
    texto_tratado = ' '.join(map(filter_impar, entrada))
    print(texto_tratado)


if __name__ == '__main__':
    main()
