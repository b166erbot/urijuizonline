# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    while True:
        try:
            input()  # na linguagem python eu nao necessito dessa entrada
            n, m = map(int, input().split())
            ma = [list(map(int, input().split())) for a in range(n)]
            le = [list(map(int, input().split())) for a in range(m)]
            c1, c2 = map(lambda x: int(x) - 1, input().split())
            atb = int(input()) - 1
            if ma[c1][atb] > le[c2][atb]:
                print('Marcos')
            elif ma[c1][atb] < le[c2][atb]:
                print('Leonardo')
            else:
                print('Empate')
        except EOFError:
            break


if __name__ == '__main__':
    main()
