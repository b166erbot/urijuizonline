# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

dici = {'suco de laranja': 120, 'morango fresco': 85,
        'mamao': 85, 'goiaba vermelha': 70, 'manga': 56,
        'laranja': 50, 'brocolis': 34}


def main():
    n = int(input())
    while n > 0:
        soma = 0
        for a in range(n):
            entrada = input()
            num, item = int(entrada.split()[0]), ' '.join(entrada.split()[1:])
            soma += num * dici[item]
        if soma in range(110, 131):
            print('{} mg'.format(soma))
        elif soma > 130:
            print('Menos {} mg'.format(soma-130))
        else:
            print('Mais {} mg'.format(110-soma))
        n = int(input())


if __name__ == '__main__':
    main()
