# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    for a in range(int(input())):
        print(len(str(pow(*[int(a) for a in input().split()]))))


if __name__ == '__main__':
    main()
