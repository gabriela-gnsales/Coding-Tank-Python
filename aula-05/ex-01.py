'''
Faça um programa que pede para a usuária digitar dois números, inicio e fim.

O seu programa deverá preencher uma lista com todos os números no intervalo (inclusive os valores inicial e final) e exibi-la na tela.
'''

inicio = int(input('Digite o valor inicial: '))
fim = int(input('Digite o valor final: '))

lista = []

for i in range(inicio, fim + 1):
    lista.append(i)

for i in range(inicio, fim-1, -1):
    lista.append(i)

print(f'Lista: {lista}')

# if inicio > fim:
#     for i in range(inicio, fim+1):
#         lista.append(i)
# else:
#     for i in range(inicio, fim-1, -1):
#         lista.append(i)
