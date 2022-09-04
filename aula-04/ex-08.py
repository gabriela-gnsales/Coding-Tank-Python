'''
Faça um programa que pergunta para a usuária com quantos termos ela gostaria de fazer a conta. Seu programa deverá calcular π utilizando a fórmula de Leibniz com a quantidade de termos especificada pela usuária.

Desafio: quando seu programa estiver pronto, experimente alguns valores e veja quantos termos são necessários para determinar o valor de π com uma precisão que você considere satisfatória.
'''

numero = int(input('Informe o número de termos que deseja fazer a conta de π pela Fórmula de Leibniz: '))

print('Fórmula de Leibniz:')

soma = 0
for i in range(numero):
    numerador = (-1)**i
    denominador = 2*i + 1
    resultado = numerador / denominador
    print(f'({numerador}/{denominador}) + ', end='')
    soma += resultado

print('...')

print(f'π ~ {(soma * 4):.4f}')
