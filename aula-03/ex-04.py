# Faça um programa que pede para a usuária digitar um número. O programa deverá exibir a tabuada daquele número.

numero = int(input('Informe o número que deseja saber a tabuada: '))

contador = 1

while contador <= 10:

    print(f'{numero} x {contador:<2} = {numero * contador}')

    contador += 1
