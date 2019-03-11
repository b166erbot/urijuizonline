# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    for a in range(int(input())):
        p1, es1, p2, es2 = input().split()
        soma = sum(map(int, input().split()))
        if soma % 2 == 0:
            if es1 == 'PAR':
                print(p1)
            else:
                print(p2)
        else:
            if es1 == 'IMPAR':
                print(p1)
            else:
                print(p2)


if __name__ == '__main__':
    main()
