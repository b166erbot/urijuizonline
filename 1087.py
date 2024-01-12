from operator import eq

class Dama:
    def __init__(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna
    
    def quantos_movimentos(self, linha_a_mover, coluna_a_mover):
        if linha_a_mover == self.linha and coluna_a_mover == self.coluna:
            return 0
        elif linha_a_mover == self.linha or coluna_a_mover == self.coluna:
            return 1
        elif eq(
            abs(linha_a_mover - self.linha),
            abs(coluna_a_mover - self.coluna)
        ):
            return 1
        else:
            return 2


def main():
    lista = []
    while True:
        a, b, c, d = map(int, input().split())
        if not any((a, b, c, d)):
            break
        lista.append((a, b, c, d))
    for (a, b, c, d) in lista:
        print(Dama(a, b).quantos_movimentos(c, d))


if __name__ == '__main__':
    main()