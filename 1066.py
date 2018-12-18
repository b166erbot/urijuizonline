# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    par = impar = positivo = negativo = 0
    for a in range(5):
        valor = int(input())
        if valor < 0:
            negativo += 1
        elif valor > 0:
            positivo += 1
        if valor % 2 == 0:
            par += 1
        else:
            impar += 1
    print('{} valor(es) par(es)\n{} valor(es) impar(es)\n'.format(par, impar) +
          '{} valor(es) positivo(s)'.format(positivo) +
          '\n{} valor(es) negativo(s)'.format(negativo))


if __name__ == '__main__':
    main()
