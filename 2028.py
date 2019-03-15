# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    caso = 0
    while True:
        try:
            lista = []
            n = int(input())
            caso += 1
        except EOFError:
            break
        if n == 0:
            print('Caso {}: 1 numero'.format(caso) + '\n0\n')
            continue
        if n == 1:
            print('Caso {}: 2 numeros'.format(caso) + '\n0 1\n')
            continue
        else:
            lista = ['0', '1']
            for a in range(2, n+1):
                lista += [str(a) for b in range(a)]
            print('Caso {}: {} numeros'.format(caso, len(lista)))
            print(' '.join(lista) + '\n')


if __name__ == '__main__':
    main()
