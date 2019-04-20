# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    for a in range(1, int(input()) + 1):
        tag, num = input(), list(map(int, input().split()))
        if tag == 'min':
            print('Caso #{}: {}'.format(a, min(num)))
        elif tag == 'max':
            print('Caso #{}: {}'.format(a, max(num)))
        elif tag == 'eye':
            num = zip(num, [0.30, 0.59, 0.11])
            soma = int(sum([(lambda x, y: x * y)(*a) for a in num]))
            print('Caso #{}: {}'.format(a, soma))
        elif tag == 'mean':
            print('Caso #{}: {}'.format(a, int(sum(num)/len(num))))


if __name__ == '__main__':
    main()
