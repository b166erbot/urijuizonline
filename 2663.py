# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    lista = []
    a, b = int(input()), int(input())
    for a in range(a):
        lista.append(int(input()))
    individuais = sorted(list(set(lista)), key=lambda x: x)
    soma = 0
    while soma < b:
        soma += lista.count(individuais.pop())
    print(soma)


if __name__ == '__main__':
    main()
