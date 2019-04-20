# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
# wrong answer (10%) por erro de precisão em ponto flutuante por causa da lin-
# guagem python. para contornar eu tentei usar a lib decimal mas sem sucesso.


def main():
    forma = 'A = {0:{4}}, B = {1:{4}}\nC = {2:{4}}, D = {3:{4}}'
    a, b = map(float, input().split())
    c, d = map(float, input().split())
    for z in ['.06F', '.01F', '.02F', '.03F', '.3E', '.0F']:
        print(forma.format(a, b, c, d, z))


if __name__ == '__main__':
    main()
