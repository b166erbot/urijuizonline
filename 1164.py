# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    distancia = int(input())
    if 1 <= distancia <= 20:
        for a in range(distancia):
            valor = int(input())
            soma = 0
            if 1 <= valor <= pow(10, 8):
                for b in range(1, valor):
                    if valor % b == 0:
                        soma += b
                if soma == valor:
                    print('{} eh perfeito'.format(valor))
                else:
                    print('{} nao eh perfeito'.format(valor))


if __name__ == '__main__':
    main()
