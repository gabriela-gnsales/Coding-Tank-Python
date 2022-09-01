'''
Faça um programa que pergunta para a usuária:

- a razão de uma PA
- o termo inicial da PA
- quantos termos ela gostaria de ver na tela

O seu programa deverá calcular e exibir os "n" termos solicitados pela usuária.
'''

razao = int(input('Qual o valor da razão da P.A.? '))
termo_i = int(input('Qual o valor do termo inicial da P.A.? '))
n_termos = int(input('Quantos termos dessa P.A. você gostaria de ver na tela? '))

termo_f = termo_i + (n_termos-1) * razao

for i in range(termo_i, termo_f+1, razao):
    print(f'{i} -> ', end='')

print('FIM')
