# -*- coding: utf-8 -*-

# não entendi o porque essa resposta não foi aceita mesmo tendo passado em
# todos os testes do udebugger (debugador uri). portanto, vai ficar essa mesmo

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    partida = {'inter': 0, 'gremio': 0, 'empate': 0}
    while True:
        a, b = [int(c) for c in input().split()]
        if a > b:
            partida['inter'] += 1
        elif a < b:
            partida['gremio'] += 1
        else:
            partida['empate'] += 1
        novo = int(input('Novo grenal (1-sim 2-nao)'))
        while novo not in [1, 2]:
            novo = int(input('Novo grenal (1-sim 2-nao)'))
        if novo == 2:
            print('{} grenais'.format(sum(partida.values())))
            print('Inter:{}'.format(partida['inter']))
            print('Gremio:{}'.format(partida['gremio']))
            print('Empates:{}'.format(partida['empate']))
            if partida['inter'] > partida['gremio']:
                print('Inter venceu mais')
            elif partida['gremio'] > partida['inter']:
                print('Gremio venceu mais')
            else:
                print('Nao houve vencedor')
            break


if __name__ == '__main__':
    main()
