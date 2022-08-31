'''
Faça um programa que pede para a usuária digitar um número inteiro positivo. O programa deverá calcular e exibir na tela o fatorial do número digitado.

Lembrete: o fatorial de um número "n", denotado por "n!", é o produto dele com todos os seus antecessores inteiros positivos.
'''

numero = int(input('Informe um número inteiro positivo: '))

while numero < 0:

    print('ERRO! O número deve ser um inteiro positivo.')

    numero = int(input('Informe novamente um número: '))

fatorial = 1

n = numero

while n > 0:

    fatorial *= n

    n -= 1

print(f'{numero}! = {fatorial}')
