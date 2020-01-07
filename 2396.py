# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    quantidade_carros = int(input().split()[0])
    vezes = range(1, quantidade_carros + 1)
    dicio = {x: sum(map(int, input().split())) for x in vezes}
    primeiras_posicoes = sorted(dicio.items(), key=lambda x: x[1])[:3]
    print('\n'.join(map(lambda x: str(x[0]), primeiras_posicoes)))


if __name__ == '__main__':
    main()
