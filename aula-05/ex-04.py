'''
Faça um programa que calcula a média dos números de uma lista numérica.
'''

from random import randint

n = int(input('Informe o tamanho da lista (nº de elementos): '))

lista = []

for i in range(n):
    lista.append(randint(0, 100))

print('Lista completa:', lista)

soma = 0
for i in lista:
    soma += i

print(f'Média dos números da lista = {soma / n}')
