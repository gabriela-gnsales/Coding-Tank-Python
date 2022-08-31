# Faça um programa que pede para a usuária digitar um número inteiro positivo. Seu programa deverá responder a soma de do número com todos os seus antecessores positivos.

numero = int(input('Informe um número inteiro positivo: '))

soma = 0

while numero > 0:

    soma += numero

    numero -= 1

print('Soma =', soma)
