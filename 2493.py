# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from operator import add, sub, mul

dici = {'+': add, '-': sub, '*': mul}


def todos(x, y, z):
    return not all([x + y != z, x - y != z, x * y != z])


def main():
    while True:
        try:
            n, j, naopass = [], [], []
            entrada = range(int(input()))
            for a in entrada:
                n.append(list(map(int, input().replace('=', ' ').split())))
            for a in entrada:
                j.append(input().split())
            for a, b in zip(n, j):
                if b[2] == 'I':
                    if todos(*n[int(b[1])-1]):
                        naopass.append(b[0])
                elif (lambda x, y, z: dici[b[2]](x, y) != z)(*n[int(b[1])-1]):
                    naopass.append(b[0])
            if len(naopass) == len(j):
                print('None Shall Pass!')
            elif any(naopass):
                print(' '.join(sorted(naopass)))
            else:
                print('You Shall All Pass!')
        except EOFError:
            break


if __name__ == '__main__':
    main()
