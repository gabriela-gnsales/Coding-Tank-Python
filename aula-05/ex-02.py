'''
Faça um programa que preenche uma lista inicialmente vazia com 20 números aleatórios entre 0 e 100.
'''

from random import randint

lista = []

for i in range(20):
    sorteio = randint(0, 100)
    lista.append(sorteio)

print(f'Lista de tamanho {len(lista)}: {lista}')

