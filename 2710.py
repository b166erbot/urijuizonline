# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
# Time limit exceeded


def main():
    lista = []
    for a in range(int(input())):
        entrada = input().split()
        if entrada[0] == 'U':
            b, c, d, e, f = [int(z) for z in entrada[1:]]
            lista.append((range(b, d + 1), range(c, e + 1), f))
        else:
            a, b = [int(a) for a in entrada[1:]]
            soma = sum([e for c, d, e in lista if a in c and b in d])
            print(soma)


if __name__ == '__main__':
    main()
