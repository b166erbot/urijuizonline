# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    lista = input().split()
    lista2 = input().split()
    x1, y1 = [float(item) for item in lista]
    x2, y2= [float(item) for item in lista2]
    distancia = (pow(x1 - x2, 2) + pow(y1 - y2, 2))**0.5
    print('{:.4f}'.format(distancia))


main()
