# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from operator import ne, gt, lt  # noqa


def main():
    input()
    # vai ficar assim pois o python não necessita da primeira entrada.
    n = list(map(int, input().split()))
    n = [(n[a], n[a+1]) for a in range(len(n)-1)]
    if gt(*n[0]):
        n = [gt(*n[a]) if a % 2 == 0 else lt(*n[a]) for a in range(len(n))]
    elif lt(*n[0]):
        n = [lt(*n[a]) if a % 2 == 0 else gt(*n[a]) for a in range(len(n))]
    else:
        return print(0)
    print(1 if all(n) else 0)


if __name__ == '__main__':
    main()
