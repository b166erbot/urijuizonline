# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    while True:
        lista = []
        try:
            for a in range(int(input())):
                lista.append((lambda x, y: (x, int(y)))(*input().split()))
            print(*[a[0] for a in sorted(lista, key=lambda x: x[1])])
        except EOFError:
            break


if __name__ == '__main__':
    main()
