# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    while True:
        try:
            entrada = input()
            resultado = verificar_parenteses(entrada)
            print('correct' if resultado else 'incorrect')
        except EOFError:
            break


def verificar_parenteses(entrada: str):
    número_contagem = 0
    for caracter in entrada:
        if caracter == '(':
            número_contagem += 1
        elif caracter == ')':
            número_contagem -= 1
        if número_contagem != 0:
            return False
    return True


main()
