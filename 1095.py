# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    i, j = 1, 60
    for a in range(j // 5):
        print('I={} J={}'.format(i, j))
        i += 3
        j -= 5
    print('I={} J={}'.format(i, j))


if __name__ == '__main__':
    main()
