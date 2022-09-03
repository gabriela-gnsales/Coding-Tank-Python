'''
Faça um programa que percorre uma lista de números. Os números abaixo da média dos valores deverão ser inseridos em uma lista, e os valores acima da média deverão ser inseridos em outra lista.
'''

from random import randint

n = int(input('Informe o tamanho da lista (nº de elementos): '))

lista = []
lista_menor = []
lista_maior = []

for i in range(n):
    lista.append(randint(1, 100))
print('Lista completa:', lista)

soma = 0
for i in lista:
    soma += i
media = soma / n
print(f'Média dos {n} números da lista = {media:.2f}')

for i in lista:
    if i < media:
        lista_menor.append(i)
    else:
        lista_maior.append(i)
print(f'Lista com {len(lista_menor)} valores ABAIXO da média: {lista_menor}')
print(f'Lista com {len(lista_maior)} valores ACIMA da média: {lista_maior}')
