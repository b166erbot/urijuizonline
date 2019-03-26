# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    lista = []
    lista2 = []
    lista3 = ['Pontos de Saque: {:.2f} %.', 'Pontos de Bloqueio: {:.2f} %.',
              'Pontos de Ataque: {:.2f} %.']
    for a in range(int(input())):
        input()
        lista.append(map(int, input().split()))
        lista2.append(map(int, input().split()))
    for a, b, c in zip(zip(*lista), zip(*lista2), lista3):
        print(c.format((sum(b) * 100) / sum(a)))


if __name__ == '__main__':
    main()
