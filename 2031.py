# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    dici = {'ataque': 2, 'pedra': 1, 'papel': 0}
    for a in range(int(input())):
        valor = input()
        valor2 = input()
        if valor == valor2:
            if valor == 'pedra':
                print('Sem ganhador')
            elif valor == 'papel':
                print('Ambos venceram')
            else:
                print('Aniquilacao mutua')
        elif dici[valor] > dici[valor2]:
            print('Jogador 1 venceu')
        else:
            print('Jogador 2 venceu')


if __name__ == '__main__':
    main()
