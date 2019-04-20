# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
# Wrong answer (10%) porque o caracter ’ não é igual ao ' e o problema
# fica dando erro quando envio. este exercício está errado para python3.4.3


def primo(x):
    divisoes = 0
    for a in range(1, x + 1):
        if x / a == x // a:
            divisoes += 1
    return divisoes == 2


def main():
    f = 'Bad boy! I\'ll hit you.'
    f2 = 'You\'re a coastal aircraft, Robbie, a large silver aircraft.'
    while True:
        try:
            lista = []
            for a in range(int(input())):
                lista.append(int(input()))
            temp = primo(sum(lista[::-int(input())]))
            print(f2 if temp else f)
        except EOFError:
            break


if __name__ == '__main__':
    main()
