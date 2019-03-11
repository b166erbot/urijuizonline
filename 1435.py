# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def formatar(lista):
    texto = '{:>4s}' * len(lista)
    return texto.format(*lista)[1:]

def main():
    n = int(input())
    if 0 <= n <= 100:
        numeros = []
        while n > 0:
            numeros.append(n)
            n = int(input())
        for z in numeros:
            lista = []
            if z == 1:
                print('  1\n')
                continue
            for a in range(1, z // 2 + 1):
                texto = []
                for b in range(1, a + 1):
                    texto.append(str(b))
                texto += [str(b)] * (z // 2 - len(texto))
                if all([z % 2 == 1, len(texto) < z]):
                    texto.append(str(b))
                    texto += texto[:-1][::-1]
                else:
                    texto += texto[::-1]
                lista.append(texto)
            novaLista = lista[::-1]
            if z % 2 == 1:
                lista += [lista[-1]]
                temp = lista[-1][:]
                temp[len(temp) // 2] = str(int(temp[len(temp) // 2]) + 1)
                lista[-1] = temp
            lista += novaLista
            print(*map(formatar, lista), sep='\n')
            print()


if __name__ == '__main__':
    main()

