# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    while True:
        try:
            a, b = map(int, input().split())
            item, count = str(b) + ' 0', 0
            for c in range(int(a)):
                if item == input():
                    count += 1
            print(count)
        except EOFError:
            break


if __name__ == '__main__':
    main()
