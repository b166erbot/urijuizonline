# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

dici = {'=.===': 'a', '===.=.=.=': 'b', '===.=.===.=': 'c', '===.=.=': 'd',
        '=': 'e', '=.=.===.=': 'f', '===.===.=': 'g', '=.=.=.=': 'h',
        '=.=': 'i', '=.===.===.===': 'j', '===.=.===': 'k', '=.===.=.=': 'l',
        '===.===': 'm', '===.=': 'n', '===.===.===': 'o', '=.===.===.=': 'p',
        '===.===.=.===': 'q', '=.===.=': 'r', '=.=.=': 's', '===': 't',
        '=.=.===': 'u', '=.=.=.===': 'v', '=.===.===': 'w', '===.=.=.===': 'x',
        '===.=.===.===': 'y', '===.===.=.=': 'z'}


def main():
    for a in range(int(input())):
        morse, texto = input().split('.......'), ''
        for b in morse:
            for c in b.split('...'):
                texto += dici[c]
            texto += ' '
        print(texto.strip())


if __name__ == '__main__':
    main()
