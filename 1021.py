# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
# este código não passa na uri porém resolve o problema da mesma forma.
# portanto, esse código vai ficara qui queira a uri sim ou não.


def main():
    notas = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0]
    moedas = [1.0, 0.50, 0.25, 0.10, 0.05, 0.01]
    valor = float(input())
    if not 0 <= valor <= 1000000.0:
        return
    print('NOTAS:')
    for cedula in notas:
        soma = 0
        while cedula <= valor:
            soma += 1
            valor -= cedula
        print('{} nota(s) de R$ {:.2f}'.format(soma, cedula))
    print('MOEDAS:')
    for moeda in moedas:
        soma = 0
        while moeda <= valor:
            soma += 1
            valor -= moeda
        print('{} moeda(s) de R$ {:.2f}'.format(soma, moeda))


main()
