# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    texto = [input() for a in range(int(input()))]
    for a in range(int(input())):
        p = input()
        sugestoes = sorted([x for x in texto if x.startswith(p)], key=len)
        if any(sugestoes):
            print(len(sugestoes), len(sugestoes[-1]))
        else:
            print(-1)


if __name__ == '__main__':
    main()
