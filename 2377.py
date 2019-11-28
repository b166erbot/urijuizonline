# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    comprimento, distancia = map(int, input().split())
    custo_km, pedagio = map(int, input().split())
    total = comprimento * custo_km + comprimento // distancia * pedagio
    print(total)


if __name__ == '__main__':
    main()
