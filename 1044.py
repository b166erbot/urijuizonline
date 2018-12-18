# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def main():
    n = [int(num) for num in input().split()]
    if not max(n) % min(n):
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')


main()
