# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    while True:
        try:
            imprimir = True
            for a in range(int(input().split()[1])):
                data, *entrada = input().split()
                if all(map(int, entrada)) and imprimir:
                    imprimir = False
                    print(data)
            if imprimir:
                print('Pizza antes de FdI')
        except EOFError:
            break


if __name__ == '__main__':
    main()
