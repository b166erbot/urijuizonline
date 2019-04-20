# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


class Ppt:
    def __init__(self, nome, mata, morre):
        self.nome = nome
        self.mata = mata
        self.morre = morre

    def __ne__(self, other):
        if other.nome == self.mata:
            return True
        elif other.nome == self.morre:
            return False


def main():
    j = {'pedra': Ppt('pedra', 'tesoura', 'papel'),
         'papel': Ppt('papel', 'pedra', 'tesoura'),
         'tesoura': Ppt('tesoura', 'papel', 'pedra')}
    q = {0: 'Os atributos dos monstros vao ser inteligencia, sabedoria...',
         1: 'Iron Maiden\'s gonna get you, no matter how far!',
         2: 'Urano perdeu algo muito precioso...',
         3: 'Putz vei, o Leo ta demorando muito pra jogar...'}
    while True:
        try:
            ent = input().split()
            i2 = list(filter(lambda x: ent.count(x) == 2, j))
            i1 = list(filter(lambda x: ent.count(x) == 1, j))
            i1 = 0 if not i1 else i1[0]
            i2 = 0 if not i2 else i2[0]
            if all((i2, i1)):
                print(q[ent.index(i1)] if j[i1] != j[i2] else q[3])
            else:
                print(q[3])
            # elif ent[0] != ent[1] != ent[2]:
            #     print('Putz vei, o Leo ta demorando muito pra jogar...')
            # elif ent[0] == ent[1] == ent[2]:
            #     print('Putz vei, o Leo ta demorando muito pra jogar...')
            # else:
            #     temp = [j[a] for a in ent]
            #     temp = temp.index((lambda x, y, z: x != y != z)(*temp))
            #     print(q[temp])
        except EOFError:
            break


if __name__ == '__main__':
    main()
