# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from operator import sub


def passo(l):
    return [l[b: b+1] for b in range(len(l)-1)]


def main():
    salto = int(input().split()[0])
    # vai ficar assim pois no python eu não necessito do segundo número
    canos = list(map(int, input().split()))
    canos = (lambda x: [x[a: a+2] for a in range(len(x)-1)])(canos)
    if all(map(lambda x: abs(sub(*x)) <= salto, canos)):
        print('YOU WIN')
    else:
        print('GAME OVER')


if __name__ == '__main__':
    main()
