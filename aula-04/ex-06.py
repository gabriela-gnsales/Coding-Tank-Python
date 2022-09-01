'''
Faça um programa que pergunta para a usuária:

- a razão de uma PG
- o termo inicial da PG
- quantos termos ela gostaria de ver na tela

O seu programa deverá calcular e exibir os "n" termos solicitados pela usuária.
'''

razao = int(input('Qual o valor da razão da P.G.? '))
termo_i = int(input('Qual o valor do termo inicial da P.G.? '))
n_termos = int(input('Quantos termos dessa P.G. você gostaria de ver na tela? '))

for i in range(n_termos):
    print(f'{termo_i} -> ', end='')
    termo_i *= razao

print('FIM')

'''
# OUTRO MODO

pg = [termo_i * razao ** (n - 1) for n in range(1, n_termos + 1)]

print(pg)
'''
