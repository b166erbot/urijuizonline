# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    valor = int(input())
    notas = [100, 50, 20, 10, 5, 2, 1]
    print(valor)
    for nota in notas:
        soma = 0
        while nota <= valor:
            soma += 1
            valor -= nota
        print('{} nota(s) de R$ {},00'.format(soma, nota))


main()
