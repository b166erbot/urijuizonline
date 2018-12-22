# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    notas = []
    while True:
        entrada = float(input())
        if 0 < entrada <= 10:
            notas.append(entrada)
        else:
            print('nota invalida')
        if len(notas) == 2:
            print('media = {:.2f}'.format(sum(notas) / len(notas)))
            break


if __name__ == '__main__':
    main()
