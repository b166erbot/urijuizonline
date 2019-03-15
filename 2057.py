# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    horas = list(range(24))
    somar = map(int, input().split())
    print(horas[sum(somar) % 24])


if __name__ == '__main__':
    main()
