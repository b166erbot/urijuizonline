# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    while True:
        try:
            for a in range(int(input())):
                colunas = []
                for a in range(int(input())):
                    colunas.append(set(map(int, input().split()[1:])))
                for a in range(int(input())):
                    x, y, z = map(int, input().split())
                    if x == 1:
                        print(len(colunas[y-1] & colunas[z-1]))
                    else:
                        print(len(colunas[y-1] | colunas[z-1]))
        except:
            break


if __name__ == '__main__':
    main()
