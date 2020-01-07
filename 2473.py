# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    dicionario = {3: 'terno', 4: 'quadra', 5: 'quina', 6: 'sena'}
    conjunto1 = set(map(int, input().split()))
    conjunto2 = set(map(int, input().split()))
    acertos = len(conjunto1 & conjunto2)
    print(dicionario.get(acertos, 'azar'))


if __name__ == '__main__':
    main()
