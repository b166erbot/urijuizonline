# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    input()
    # o python nao necessita desta primeira entrada.
    n = list(map(int, input().split()))
    n = [n[a] > n[a+1] for a in range(len(n)-1)]
    if True in n:
        print(n.index(True) + 2)
    else:
        print(0)


if __name__ == '__main__':
    main()
