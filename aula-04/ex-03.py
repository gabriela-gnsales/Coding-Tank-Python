'''
Faça um programa que pede para a usuária digitar um número inteiro positivo. O programa deverá utilizar um laço do tipo for para calcular e exibir na tela o fatorial do número digitado.
'''

numero = int(input('Informe o número que deseja saber o fatorial: '))

while numero < 0:
    print('Opção inválida!')
    numero = int(input('Informe um número inteiro positivo: '))

print(f'Fatorial: {numero}! = ', end='')
fatorial = 1
for i in range(1, numero+1):
    print(i, end='')
    print(' x ' if i < numero else ' = ', end='')
    fatorial *= i
print(fatorial)

print('-' * 50)

# OUTRO MODO DE EXIBIÇÃO

print(f'Fatorial: {numero}! = ', end='')
fatorial = 1
for i in range(numero, 0, -1):
    print(i, end='')
    print(' x ' if i > 1 else ' = ', end='')
    fatorial *= i
print(fatorial)
