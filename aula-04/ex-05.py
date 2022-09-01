'''
Faça um programa que pergunta para a usuária:

- a razão de uma PA
- o termo inicial da PA
- quantos termos ela gostaria de ver na tela

O seu programa deverá calcular e exibir os "n" termos solicitados pela usuária.
'''

razao = int(input('Qual o valor da razão da P.A.? '))
termo_i = int(input('Qual o termo inicial da P.A.? '))
termo_f = int(input('Quantos termos dessa P.A. você gostaria de ver na tela? '))

for n in range(1, termo_f+1):
    if n == 1:
        termo_n = termo_i
    else:
        termo_n = termo_i + razao
    print(f'{n:2}º termo da P.A.: {termo_n}')
    termo_i = termo_n
'''
for n in range(1, termo_f+1):
    termo_n = termo_i + (n-1) * razao
    print(f'a_{n} = {termo_n}')
'''
