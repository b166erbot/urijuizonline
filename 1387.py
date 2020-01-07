# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    # sei la o porque eu estou fazendo esse exercicio.
    entrada = list(map(int, input().split()))
    while entrada != [0, 0]:
        print(sum(entrada))
        entrada = list(map(int, input().split()))


if __name__ == '__main__':
    main()
