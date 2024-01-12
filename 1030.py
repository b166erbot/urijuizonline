# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# import sys


# sys.setrecursionlimit(100000)


# def josephus(n, k):
#     if n == 1:
#         return 1
#     return (josephus(n - 1, k) + k-1) % n + 1


# def main():
#     for x in range(1, int(input()) + 1):
#         n, k = map(int, input().split())
#         print('Case {}: {}'.format(x, josephus(n, k)))



class Contagem:
    def __init__(self, número_final: int, salto: int) -> None:
        pass



class Josephus:
    def __init__(self, número_final: int, salto: int):
        self._itens = list(range(1, número_final + 1))
        self._salto = salto
        self._contagem = -1
        self.número_maximo = número_final
    
    def _avançar(self) -> int:
        """Avança a contagem circularmente e retorna um número."""
        return (self._contagem + self._salto) % self.número_maximo

    def dropar_proximo(self) -> int:
        """Dropa um número em específico."""
        self._contagem = self._avançar()
        número_dropado =  self._itens.pop(self._contagem)
        # removeu um item, desacrescenta 1 na _contagem
        self._contagem -= 1
        self.número_maximo -= 1
        return número_dropado

    def retornar_último_número(self) -> int:
        """Dropa todos os números conforme o salto e retorna o último número."""
        while self.número_maximo > 0:
            resultado = self.dropar_proximo()
        return resultado


def main():
    for contagem in range(1, int(input()) + 1):
        número_final, salto = map(int, input().split())
        objeto_josephus = Josephus(número_final, salto)
        resultado = objeto_josephus.retornar_último_número()
        print(f"Case {contagem}: {resultado}")


if __name__ == '__main__':
    main()
