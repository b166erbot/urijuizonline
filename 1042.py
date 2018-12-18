# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def main():
    numeros = [int(a) for a in input().split()]
    numeros_sorted = numeros[:]
    numeros_sorted.sort()
    for numero in numeros_sorted:
        print(numero)
    print()
    for numero in numeros:
        print(numero)


main()
