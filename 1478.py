# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def formatar(lista):
    texto = '{:>4}' * len(lista)
    return texto.format(*lista)[1:]


def main():
    e = int(input())
    numeros = []
    while 0 < e <= 100:
        numeros.append(e)
        e = int(input())
    for b in numeros:
        lista = [abs(a) for a in range(-b, b+1) if a not in [0, 1]]
        for a in range(b):
            print(formatar(lista[a: a+b][::-1]))
        print()


if __name__ == '__main__':
    main()
