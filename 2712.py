# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
import re

semana = {'12': 'MONDAY', '34': 'TUESDAY', '56': 'WEDNESDAY',
          '78': 'THURSDAY', '90': 'FRIDAY'}


def main():
    regex = re.compile(r'^[A-Z]{3}-\d{4}$')
    for a in range(int(input())):
        result = re.findall(regex, input())
        if result:
            print(semana[next(filter(lambda x: result[0][-1] in x, semana))])
        else:
            print('FAILURE')


if __name__ == '__main__':
    main()
