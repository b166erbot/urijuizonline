# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    int(input())  # sinceramente, não sei o porque disso nesse exercício.
    # colocar um número sendo que eu não utilizarei ele para nada.
    # eu poderia fazer até uma verificação para ver se a lista continha
    # o mesmo tamanho da primeira input, mas é trabalho desnecessário
    # pois o uri não cobra a verificação do mesmo.
    # portanto, ficará assim por motivos óbvios, falta de necessidade e
    # mesmo se fosse implementado, não daria erro o programa.
    n = list(map(int, input().split()))
    print(n.index(min(n)) + 1)


if __name__ == '__main__':
    main()
