'''
Faça um programa que pede para a usuária digitar um número inteiro positivo. Seu programa deverá utilizar um laço do tipo for para responder a soma de do número com todos os seus antecessores positivos.
'''

numero = int(input('Informe um número inteiro positivo: '))

soma = 0
for i in range(1, numero+1):
    soma += i
    # print('i:', i, ' - soma:', soma)

print(f'A soma do número {numero} com todos os seus antecessores positivos é igual a {soma}.')

