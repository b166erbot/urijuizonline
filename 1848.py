# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    count = 0
    n = 0
    while count < 3:
        resposta = input()
        if resposta == 'caw caw':
            count += 1
            print(n)
            n = 0
        else:
            resposta = resposta.replace('-', '0').replace('*', '1')
            n += int(resposta, 2)


if __name__ == '__main__':
    main()
