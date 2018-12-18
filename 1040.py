# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def main():
    lista = [float(a) for a in input().split()]
    lista = [lista[a] * [2, 3, 4, 1][a] for a in range(4)]
    media = sum(lista) / 10
    if 5 <= media <= 6.9:
        exame = float(input())
    print('Media: {:.1f}'.format(media))
    if media >= 7:
        print('Aluno aprovado.')
    elif media < 5:
        print('Aluno reprovado.')
    else:
        print('Aluno em exame.')
        print('Nota do exame: {:.1f}'.format(exame))
        media_final = (exame + media) / 2
        if media_final >= 5:
            print('Aluno aprovado.')
        else:
            print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(media_final))


main()
