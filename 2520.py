# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    while True:
        try:
            lista = []
            for a in range(1, int(input().split()[0]) + 1):
                e = input().split()
                if '1' in e:
                    lista.append([a, e.index('1') + 1])
                if '2' in e:
                    lista.append([a, e.index('2') + 1])
            print(sum(map(lambda x: abs(x[0] - x[1]), zip(*lista))))
        except EOFError:
            break


if __name__ == '__main__':
    main()
