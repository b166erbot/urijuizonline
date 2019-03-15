# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from datetime import datetime


def main():
    chegada = datetime.strptime('7:00', '%H:%M')
    while True:
        try:
            entrada = input()
        except EOFError:
            break
        tempo = datetime.strptime(entrada, '%H:%M')
        if tempo > chegada:
            resultado = tempo - chegada
            print('Atraso maximo: {}'.format(resultado.seconds // 60))
        else:
            print('Atraso maximo: 0')


if __name__ == '__main__':
    main()
