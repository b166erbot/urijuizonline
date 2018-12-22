# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    n = 1
    idades = []
    while n > 0:
        n = int(input())
        if n > 0:
            idades.append(n)
    print('{:.2f}'.format(sum(idades) / len(idades)))

if __name__ == '__main__':
    main()
