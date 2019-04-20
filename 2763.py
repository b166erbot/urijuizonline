# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
import re


def main():
    regex = re.compile(r'\d+')
    result = re.findall(regex, input())
    print(*result, sep='\n')


if __name__ == '__main__':
    main()
