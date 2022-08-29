'''
Faça um programa que pergunta o comprimento de cada um dos 3 lados de um triângulo.

O programa deverá responder:

- É triângulo, caso nenhum dos lados possua comprimento superior à soma dos outros dos lados.

- Não é triângulo, caso um dos lados seja possua comprimento superior à soma dos outros dois lados.

Exemplos:

Se os lados forem 3, 4 e 5, o triângulo existe, pois:

5 < 3 + 4
4 < 3 + 5
3 < 4 + 5
Se os lados forem 6, 10 e 6, o triângulo também existe:

6 < 10 + 6
6 < 10 + 6
10 < 6 + 6
Já se os supostos lados forem 2, 5 e 2, o triângulo não existe, pois:

5 > 2 + 2
'''

lado1 = float(input('Qual o comprimento do lado 1 do triângulo? '))

lado2 = float(input('Qual o comprimento do lado 2 do triângulo? '))

lado3 = float(input('Qual o comprimento do lado 3 do triângulo? '))

if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2):

    print('É triângulo!')

else:

    print('Não é triângulo!')
