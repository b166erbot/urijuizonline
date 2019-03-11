# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    input()
    # vai ficar assim pois o python nao necessita
    # do primeiro input para funcionar
    numeros = list(map(int, input().split()))
    index, estrelas = 0, 0
    stop = False
    while len(numeros) > index > -1:
        if numeros[index] % 2 == 1:
            numeros[index] -= 1 if numeros[index] else 0
            index += 1
            if not stop:
                estrelas += 1
        else:
            numeros[index] -= 1 if numeros[index] else 0
            index -= 1
            if not stop:
                estrelas += 1
                stop = True
    print(estrelas, sum(numeros))


if __name__ == '__main__':
    main()
