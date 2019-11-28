# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def chunk(lista, tamanho):
    return [sum(lista[x:tamanho + x]) for x in range(len(lista) - 1)]


class Pascal:
    def __init__(self, vezes):
        self.lista = [1]
        self.vezes = vezes - 1
        self.salto = 2
        self.total = 1

    def somar(self):
        lista = chunk(self.lista, self.salto)
        lista.append(1)
        lista.insert(0, 1)
        return lista

    def rodar(self):
        if self.vezes > 0:
            self.lista.append(1)
            self.vezes -= 1
            self.total += sum(self.lista)
        while self.vezes > 0:
            self.vezes -= 1
            self.lista = self.somar()
            self.total += sum(self.lista)
        print(self.total)


def main():
    for _ in range(int(input())):
        Pascal(vezes = int(input())).rodar()


if __name__ == '__main__':
    main()
