# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    cobaias = {'C': 0, 'S': 0, 'R': 0}
    for a in range(int(input())):
        quantidade, cobaia = input().split()
        if not 1 <= int(quantidade) <= 15:
            continue
        cobaias[cobaia] += int(quantidade)
    total = sum(cobaias.values())
    porcentagem_C = (cobaias['C'] * 100) / total
    porcentagem_R = (cobaias['R'] * 100) / total
    porcentagem_S = (cobaias['S'] * 100) / total
    print('Total: {} cobaias'.format(total))
    print('Total de coelhos: {}'.format(cobaias['C']))
    print('Total de ratos: {}'.format(cobaias['R']))
    print('Total de sapos: {}'.format(cobaias['S']))
    print('Percentual de coelhos: {:.2f} %'.format(porcentagem_C))
    print('Percentual de ratos: {:.2f} %'.format(porcentagem_R))
    print('Percentual de sapos: {:.2f} %'.format(porcentagem_S))


if __name__ == '__main__':
    main()
