# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def replacer(text, dici):
    texto = ''
    for a in text:
        temp = dici.get(a.upper(), a)
        texto += temp.upper() if a.isupper() else temp.lower()
    return texto


def main():
    while True:
        try:
            n = range(int(input().split()[1]))
            entrada = [input(), input()]
            replace = dict(zip(*entrada))
            replace.update(dict(zip(*entrada[::-1])))
            for a in n:
                print(replacer(input(), replace))
            print()
        except EOFError:
            break


if __name__ == '__main__':
    main()
