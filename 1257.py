# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


from string import ascii_uppercase as z


def calcular(textos):
    total = 0
    for e, texto in enumerate(textos):
        total += sum([sum([z.index(l), e, i]) for i, l in enumerate(texto)])
    return total


def main():
    for _ in range(int(input())):
        entrada = [input() for _ in range(int(input()))]
        print(calcular(entrada))


if __name__ == '__main__':
    main()
