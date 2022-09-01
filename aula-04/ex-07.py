'''
Faça um programa que pergunta para a usuária quantos termos da sequência de Fibonacci ela gostaria de ver. O seu programa deverá calcular e exibir a quantidade de termos desejada por ela.
'''

numero = int(input('Informe o número de termos que deseja ver da sequência de Fibonacci: '))

print('Sequência de Fibonacci:')

n1 = n2 = 1
for i in range(numero):
    if i == 0 or i == 1:
        n = 1
    else:
        n = n1 + n2
    print(f'{n} -> ', end='')
    n1 = n2
    n2 = n

print('FIM')
