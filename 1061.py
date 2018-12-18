# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def mult(x, y):
    if not y:
        return x
    return x * y


def main():
    dia = int(input().split()[1])
    tempo = [int(a) for a in input().split(':')]
    dia2 = int(input().split()[1])
    tempo2 = [int(a) for a in input().split(':')]
    
    dias = dia2 - dia
    horas = tempo2[0] - tempo[0]
    minutos = tempo2[1] - tempo[1]
    segundos = tempo2[2] - tempo[2]

    if horas < 0:
        horas += 24
        dias -= 1
    if minutos < 0:
        minutos += 60
        horas -= 1
    if segundos < 0:
        segundos += 60
        minutos -= 1

    print('{} dia(s)\n{} hora(s)\n'.format(int(dias), int(horas)) +
          '{} minuto(s)\n{} segundo(s)'.format(int(minutos), int(segundos)))


if __name__ == '__main__':
    main()
