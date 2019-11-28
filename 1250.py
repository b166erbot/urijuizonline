# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    for _ in range(int(input())):
        input()
        alturas = map(int, input().split())
        pulos = input()
        total = 0
        for altura, pulo in zip(alturas, pulos):
            if pulo == 'S':
                if altura <= 2:
                    total += 1
            else:
                if altura >= 3:
                    total += 1
        print(total)


if __name__ == '__main__':
    main()
