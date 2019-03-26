# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    while True:
        try:
            lista = []
            for a in range(int(input().split()[0])):
                lista.append(''.join(input().split()).replace('1', '9'))
            for a, b in enumerate(lista):
                temp = ''
                for c, d in enumerate(b):
                    soma = 0
                    if d == '9':
                        temp += d
                    else:
                        if len(lista) - 1 > a >= 0:
                            if lista[a+1][c] == '9':
                                soma += 1
                        if len(lista) >= a > 0:
                            if lista[a-1][c] == '9':
                                soma += 1
                        if len(b) - 1 > c >= 0:
                            if b[c+1] == '9':
                                soma += 1
                        if len(b) > c > 0:
                            if b[c-1] == '9':
                                soma += 1
                        temp += str(soma)
                print(temp)
        except EOFError:
            break


if __name__ == '__main__':
    main()
