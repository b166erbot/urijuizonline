# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    for a in range(int(input())):
        i = bin(int(input())).replace('b', '').split('0')
        t = max(i, key=lambda x: len(x)).count('1')
        print(t)


if __name__ == '__main__':
    main()
