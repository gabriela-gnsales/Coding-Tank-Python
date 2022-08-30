# Faça um programa que pede para a usuária digitar um número inteiro positivo. O programa deve exibir todos os números inteiros de 0 até o número digitado.

numero = int(input('Informe um número inteiro positivo: '))

while numero <= 0:

    print('ERRO! O número deve ser um inteiro positivo.')

    numero = int(input('Informe novamente um número: '))

contador = 0

while contador <= numero:

    print(contador)

    contador += 1
