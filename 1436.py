# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def mediana(numeros):
    return sum(numeros) // 2


def main():
    for x in range(1, int(input()) + 1):
        itens = list(map(int, input().split()))
        itens.pop(0)
        quantidade = len(itens)
        meio = quantidade // 2
        if quantidade % 2 == 0:
            resposta = mediana(itens[meio, meio + 1])
        else:
            resposta = itens[meio]
        print('Case {}: {}'.format(x, resposta))


if __name__ == '__main__':
    main()
