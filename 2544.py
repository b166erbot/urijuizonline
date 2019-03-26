# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    while True:
        try:
            n, m = int(input()), 0
            if n == 1:
                print(0)
            else:
                while n > 1:
                    n /= 2
                    m += 1
                print(m)
        except EOFError:
            break


if __name__ == '__main__':
    main()
