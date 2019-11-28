# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    for _ in range(int(input())):
        a, b, c = input()
        a, c = int(a), int(c)
        if a == c:
            resultado = a * c
        elif b.isupper():
            resultado = c - a
        else:
            resultado = a + c
        print(resultado)


if __name__ == '__main__':
    main()
