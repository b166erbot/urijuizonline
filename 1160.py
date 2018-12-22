# -*- coding: utf-8 -*-
# o uri bota as condições para serem satisfeitas só para fazer a gente de burro
# se não precisava dessas condições, então porque o uri botou elas??

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    t = int(input())
    if 1 <= t <= 3000:
        for a in range(t):
            c = [float(b) for b in input().split()]
            pa, pb, g1, g2 = int(c[0]), int(c[1]), c[2], c[3]
            # condicoes = [100 <= pa <= 1000000,
            #              pa < pb <= 1000000,
            #              0.1 <= g1 <= 10,
            #              0 <= g2 <= 10]
            # if all(condicoes):
            anos = 0
            while not pa > pb:
                anos += 1
                pa = int(pa + (pa / 100) * g1)
                pb = int(pb + (pb / 100) * g2)
                if anos > 100:
                    print('Mais de 1 seculo.')
                    break
            if not anos > 100:
                print('{} anos.'.format(anos))


if __name__ == '__main__':
    main()
