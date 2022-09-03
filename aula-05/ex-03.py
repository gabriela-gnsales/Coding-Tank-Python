'''
Faça um programa que percorre uma lista de números aleatórios (ver exercício 2) e exibe na tela apenas os números pares.
'''

from random import randint

n = int(input('Informe o tamanho da lista (nº de elementos): '))

lista = []

for i in range(n):
    lista.append(randint(0, 100))

print('Lista completa:', lista)

print('Números pares da lista: ', end='')
for i in lista:
    if i % 2 == 0:
        print(i, end=' - ')
print('FIM')
