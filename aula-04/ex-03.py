'''
Faça um programa que pede para a usuária digitar um número inteiro positivo. O programa deverá utilizar um laço do tipo for para calcular e exibir na tela o fatorial do número digitado.
'''

numero = int(input('Informe o número que deseja saber o fatorial: '))

while numero < 0:
    print('Opção inválida!')
    numero = int(input('Informe um número inteiro positivo: '))

fatorial = 1
for i in range(1, numero+1):
    fatorial *= i
    if i != numero:
        print(f'{i} x ', end='')
    else:
        print(f'{i}')

print(f'Fatorial: {numero}! = {fatorial}')
