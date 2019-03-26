# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from itertools import permutations


def main():
    temp = list(map(int, input().split()))
    if any(map(lambda x: x[0] + x[1] == x[2], permutations(temp, 3))):
        print('S')
    elif any(map(lambda x: temp.count(x) > 1, temp)):
        print('S')
    else:
        print('N')


if __name__ == '__main__':
    main()
