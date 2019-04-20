# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    entrada = input()
    ida, volta, gips = 0, 0, 0
    while entrada != 'ABEND':
        if 'SALIDA' in entrada:
            ida += int(entrada.split()[1])
            gips += 1
        else:
            volta += int(entrada.split()[1])
            gips -= 1
        entrada = input()
    falta = ida - volta
    print(falta, gips, sep='\n')


if __name__ == '__main__':
    main()
