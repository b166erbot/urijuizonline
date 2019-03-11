# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    numeros = []
    try:
        n = input()
        while n.isnumeric():
            if 0 < int(n) <= 70:
                numeros.append(int(n))
                n = input()
            else:
                break
    except EOFError:
        pass
    for a in numeros:
        if a == 1:
            print(2)
            continue
        elif a == 2:
            print(12, 21, sep='\n')
            continue
        lista = ['3'] * (a-2)
        lista2 = []
        for b in range(a//2):
            temp = lista[:]
            temp.insert(b, '1')
            if ~b == -1:
                temp.append('2')
            else:
                temp.insert(-b, '2')  # ~b+1
            lista2.append(temp)
        if a % 2 == 1:
            lista.append('3')
            lista.insert(a//2, '2')
            lista2 += [lista] + list(map(lambda x: x[::-1], lista2[::-1]))
        else:
            lista2 += list(map(lambda x: x[::-1], lista2[::-1]))
        print(*map(''.join, lista2), sep='\n')


if __name__ == '__main__':
    main()
