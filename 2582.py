# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

lista = ['PROXYCITY', 'P.Y.N.G.', 'DNSUEY!', 'SERVERS', 'HOST!', 'CRIPTONIZE',
         'OFFLINE DAY', 'SALT', 'ANSWER!', 'RAR?', 'WIFI ANTENNAS']


def main():
    for a in range(int(input())):
        print(lista[sum(map(int, input().split()))])


if __name__ == '__main__':
    main()
