# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


from operator import mul


def main():
    temp = [300, 1500, 600, 1000, 150]
    temp2 = [int(input()) for x in range(5)]
    print(sum(map(mul, temp, temp2)) + 225)


if __name__ == '__main__':
    main()
