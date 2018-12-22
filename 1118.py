# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    notas, novo = [], 1
    while novo == 1:
        valor = float(input())
        if 0 <= valor <= 10:
            notas.append(valor)
        else:
            print('nota invalida')
        if len(notas) == 2:
            print('media = {:.2f}'.format(sum(notas) / len(notas)))
            novo = float(input('novo calculo (1-sim 2-nao)\n'))
            while novo not in [1, 2]:
                novo = float(input('novo calculo (1-sim 2-nao)\n'))
            notas = []


if __name__ == '__main__':
    main()
