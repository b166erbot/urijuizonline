# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from itertools import cycle
from string import ascii_lowercase as s


def main():
    t = input()
    for a in range(int(input())):
        chave = cycle(t)
        resultado = ''
        texto = input().split()
        for a in texto:
            if not a[0] in 'aeiou':
                resultado += ''.join([
                    s[(s.index(next(chave)) + s.index(b)) % 26] for b in a])
            else:
                resultado += a
            resultado += ' '
        print(resultado.strip())


if __name__ == '__main__':
    main()
