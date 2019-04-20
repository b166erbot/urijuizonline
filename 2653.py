# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    joias = set()
    while True:
        try:
            joias.add(input())
        except EOFError:
            break
    print(len(joias))


if __name__ == '__main__':
    main()
