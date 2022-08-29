'''
Faça um programa que pede para a usuária digitar, separadamente, os coeficientes a, b e c de uma equação de segundo grau.

O programa deverá calcular o valor do discriminante (delta) e:

- Caso seja positivo, o programa deverá calcular e exibir na tela os valores de suas duas raizes reais e distintas.

- Caso seja zero, o programa deverá calcular e exibir na tela a sua única raiz.

- Caso seja negativo, o programa deverá exibir a mensagem Não possui raizes reais.

Dica 1: caso precise refrescar a memória com as fórmulas, este site pode ser útil.

Dica 2: elevar um número ao expoente meio (1/2 ou 0.5) equivale a calcular sua raiz quadrada. 4 elevado a (1/2) dá 2. 9 elevado a (1/2) dá 3.
'''

a = float(input("Informe o coeficiente 'a' da equação de 2º grau: "))

b = float(input("Informe o coeficiente 'b' da equação de 2º grau: "))

c = float(input("Informe o coeficiente 'c' da equação de 2º grau: "))

delta = b ** 2 - 4 * a * c

if delta > 0:

    x1 = (-b + delta ** (1/2)) / (2 * a)

    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print(f'O valor das duas raízes da equação é {x1:.2f} e {x2:.2f}.')

elif delta == 0:

    x = -b / (2 * a)

    print(f'O valor da única raiz da equação é {x:.2f}.')

else:

    print('A equação não possui raízes reais.')
