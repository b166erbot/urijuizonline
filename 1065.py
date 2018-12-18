# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def main():
    pares = 0
    for a in range(5):
        if int(input()) % 2 == 0:
            pares += 1
    print('{} valores pares'.format(pares))


if __name__ == '__main__':
    main()
