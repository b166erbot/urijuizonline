# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    try:
        while True:
            quantidade = int(input())
            lesmas = list(map(int, input().split()))
            if len(lesmas) == quantidade:
                veloz = max(lesmas)
                if veloz < 10:
                    print(1)
                elif 10 <= veloz < 20:
                    print(2)
                elif veloz >= 20:
                    print(3)
    except EOFError:
        pass


if __name__ == '__main__':
    main()
