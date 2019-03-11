# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def main():
    numeros = list(map(int, input().split()))
    while numeros != [0]:
        a, b, c = numeros
        print(int(pow(((a * b) * 100) / c, 0.5)))
        numeros = list(map(int, input().split()))


if __name__ == '__main__':
    main()
