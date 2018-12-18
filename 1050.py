# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    ddd = {61: 'Brasilia', 71: 'Salvador', 11: 'Sao Paulo',
           21: 'Rio de Janeiro', 32: 'Juiz de Fora', 19: 'Campinas',
           27: 'Vitoria', 31: 'Belo Horizonte'}
    numero = int(input())
    print('{}'.format(ddd.get(numero, 'DDD nao cadastrado')))


if __name__ == '__main__':
    main()
