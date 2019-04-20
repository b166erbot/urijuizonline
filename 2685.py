# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    lista = []
    b, c, d = [a for a in range(90)] + [360], range(90, 180), range(180, 270)
    while True:
        try:
            lista.append(int(input()))
        except EOFError:
            break
    for a in lista:
        if a in b:
            print('Bom Dia!!')
        elif a in c:
            print('Boa Tarde!!')
        elif a in d:
            print('Boa Noite!!')
        else:
            print('De Madrugada!!')


if __name__ == '__main__':
    main()
