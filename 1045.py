# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    numeros = [float(n) for n in input().split()]
    for n in numeros:
        if 0 > n:
            return
    a = numeros.pop(numeros.index(max(numeros)))
    b, c = numeros
    if a >= b + c:
        print('NAO FORMA TRIANGULO')
        return
    elif a ** 2 == b ** 2 + c ** 2:
        print('TRIANGULO RETANGULO')
    elif a ** 2 > b ** 2 + c ** 2:
        print('TRIANGULO OBTUSANGULO')
    elif a ** 2 < b ** 2 + c ** 2:
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or a == c or b == c:
        print('TRIANGULO ISOSCELES')


main()
