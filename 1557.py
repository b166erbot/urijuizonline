# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def formate(forma, x):
    return forma.format(*x)[1:]


def main():
    n = int(input())
    lista = []
    while 0 < n <= 15:
        forma = '{:>len}' * n
        lista2 = [1]
        for a in range(n-1):
            lista2.append(lista2[-1]*2)
        lista.append(lista2)
        for a in range(n-1):
            lista.append(list(map(lambda x: x*2, lista[-1])))
        forma = forma.replace('len', str(len(str(lista[-1][-1])) + 1))
        print(*[a for a in map(formate, [forma]*n, lista)], sep='\n')
        lista, n = [], int(input())
        print()


if __name__ == '__main__':
    main()
