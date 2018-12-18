# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    valor = float(input())
    if 0 < valor <= 2000:
        print('Isento')
    else:
        valor -= 2000
        if 0 < valor <= 1000:
            print('R$ {:.2f}'.format((valor / 100) * 8))
        elif 1000 < valor <= 2500:
            valor -= 1000
            print('R$ {:.2f}'.format((1000 / 100) * 8 + (valor / 100) * 18))
        elif valor > 2500:
            valor -= 2500
            resultado = (1000 / 100) * 8
            resultado += (1500 / 100) * 18 + (valor / 100) * 28
            print('R$ {:.2f}'.format(resultado))


if __name__ == '__main__':
    main()
