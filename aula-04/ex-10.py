'''
Faça um programa que pede para a usuária digitar uma base e um expoente.

O seu programa deverá responder o resultado da operação de potência entre os números digitados sem utilizar o operador ** do Python.
'''

base = float(input('Informe a base: '))
expoente = int(input('Informe o expoente: '))

n = base
for i in range(expoente-1):
    n *= base

print(f'Resultado da operação de potência: {n:.1f}')
