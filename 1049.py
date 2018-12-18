# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    dicionario = {'vertebrado': {'ave': {'carnivoro': 'aguia',
                                         'onivoro': 'pomba'},
                                 'mamifero': {'onivoro': 'homem',
                                              'herbivoro': 'vaca'}
                                 },
                  'invertebrado': {'inseto': {'hematofago': 'pulga',
                                              'herbivoro': 'lagarta'},
                                   'anelideo': {'hematofago': 'sanguessuga',
                                                'onivoro': 'minhoca'}
                                   }
                  }
    a = input()
    b = input()
    c = input()
    print('{}'.format(dicionario[a][b][c]))


if __name__ == '__main__':
    main()
