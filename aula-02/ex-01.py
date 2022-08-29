# Faça um programa que pede para a usuária digitar um número e responde se o número é positivo ou negativo.

numero = float(input('Digite um número: '))

if numero > 0:

    print('O número que você digitou é POSITIVO!')

elif numero == 0:

    print('O zero é um número neutro, ou seja, não é um número nem positivo e nem negativo.')

else:

    print('O número que você digitou é NEGATIVO!')
