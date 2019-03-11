# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from operator import ne


class Pptls:
    def __init__(self, nome, morre, morre2, mata, mata2):
        self.nome = nome
        self.morre = [morre, morre2]
        self.mata = [mata, mata2]

    def __ne__(self, other):
        if other.nome in self.morre:
            return 'Raj trapaceou!'
        elif other.nome in self.mata:
            return 'Bazinga!'
        elif self.nome == other.nome:
            return 'De novo!'

    def __str__(self):
        return '{}'.format(self.name)


def main():
    obj = {'tesoura': Pptls('tesoura', 'pedra', 'spock', 'papel', 'lagarto'),
           'papel': Pptls('papel', 'tesoura', 'lagarto', 'pedra', 'spock'),
           'pedra': Pptls('pedra', 'papel', 'spock', 'tesoura', 'lagarto'),
           'lagarto': Pptls('lagarto', 'pedra', 'tesoura', 'papel', 'spock'),
           'Spock': Pptls('spock', 'lagarto', 'papel', 'pedra', 'tesoura')}
    for a in range(1, int(input())+1):
        print('Caso #{}: {}'.format(a, ne(*map(obj.get, input().split()))))


if __name__ == '__main__':
    main()
