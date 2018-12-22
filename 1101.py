# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    conteudo = []
    while True:
        valores = [int(a) for a in input().split()]
        valores.sort()
        if valores[0] <= 0 or valores[1] <= 0:
            break
        valores[1] += 1
        lista = list(range(*valores))
        conteudo.append(lista)
    for lista in conteudo:
        print('{} Sum={}'.format(' '.join([str(a) for a in lista]), sum(lista)))


if __name__ == '__main__':
    main()
