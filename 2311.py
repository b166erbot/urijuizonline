# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    for a in range(int(input())):
        nome = input()
        dificuldade = float(input())
        notas = list(map(float, input().split()))
        notas.pop(notas.index(min(notas)))
        notas.pop(notas.index(max(notas)))
        print('{} {:.2f}'.format(nome, sum(notas) * dificuldade))


if __name__ == '__main__':
    main()
