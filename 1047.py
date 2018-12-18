# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    hi, mi, hf, mf = map(int, input('Digite horas e minutos: ').split())
    if hi == hf and mi == mf:
        print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
    else:
        ht = hf - hi
        mt = mf - mi
        if ht < 0:
            ht += 24
        if mt < 0:
            mt += 60
            ht -= 1
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(ht, mt))


if __name__ == '__main__':
    main()
