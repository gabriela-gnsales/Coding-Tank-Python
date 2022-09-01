'''
Faça um programa que pede para a usuária digitar um número. O programa deverá utilizar um laço do tipo for para exibir a tabuada daquele número.
'''

numero = int(input('Informe o número que deseja saber a tabuada: '))

for i in range(1, 11):
    print(f'{numero} x {i:<2} = {numero * i}')
