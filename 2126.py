# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    lista = []
    while True:
        try:
            lista.append([input(), input()])
        except EOFError:
            break
    n = 0
    for a, b in lista:
        n += 1
        print('Caso #{}:'.format(n))
        chunk = lambda x: [x[c: c + len(a)] for c in range(len(b)-len(a)+1)]
        selecionados = chunk(b)
        if selecionados.count(a) > 0:
            print('Qtd.Subsequencias: {}'.format(selecionados.count(a)))
            print('Pos: {}\n'.format(b.rfind(a) + 1))
        else:
            print('Nao existe subsequencia\n')


if __name__ == '__main__':
    main()
