# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    I = 0
    J = 1
    aux = 0.2
    for z in range(11):
        for w in range(3):
            if I == 0:
                print("I={} J={}".format(I, J))
            elif I == 1:
                print("I={} J={}".format(I, J))
            elif I > 1.9:
                print("I={} J={}".format(2, J))
            else:
                print("I={:.1f} J={:.1f}".format(I, J))
            J += 1
        J = 1 + aux
        I += 0.2
        aux += 0.2


if __name__ == '__main__':
    main()
