# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def triangulo(valores):
    a, b, c = valores
    condicoes = [abs(b - c) < a < b + c,
                 abs(a - c) < b < a + c,
                 abs(a - b) < c < a + b]
    if all(condicoes):
        return True
    return False
                 

def main():
    valores = [float(n) for n in input().split()]
    if triangulo(valores):
        print('Perimetro = {}'.format(sum(valores)))
    else:
        a, b, c = valores
        print('Area = {}'.format( ((a + b) * c) / 2 ))


main()
