# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from itertools import permutations as per


def main():
    temp = list(map(int, input().split()))
    c, a, b = temp.pop(temp.index(max(temp))), temp[0], temp[1]
    condicoes = [abs(b - c) < a < b + c, abs(a - c) < b < a + c,
                 abs(a - b) < c < a + b]
    if all(condicoes):
        if a == b == c:
            print('Valido-Equilatero')
        elif a != b != c:
            print('Valido-Escaleno')
        elif any(map(lambda x: x[0] == x[1] != x[2], per([a, b, c], 3))):
            print('Valido-Isoceles')
        print('Retangulo: {}'.format('S' if a**2 + b**2 == c**2 else 'N'))
    else:
        print('Invalido')


if __name__ == '__main__':
    main()
