'''
Bibliotecas ou módulos são arquivos contendo algumas funções e outros componentes de código já prontos para serem reutilizados. A linguagem Python já possui diversos módulos pré-instalados, e podemos utilizá-los através do comando import.

Ao incluir a linha abaixo (preferencialmente no topo do programa) podemos acessar as funções do módulo random, que permitem lidar com números aleatórios:

import random
Tendo importado esse módulo em nosso programa, é possível sortear números aleatórios através da função randint. No exemplo abaixo, um número aleatório entre 1 e 100 é salvo na variável "sorteio":

sorteio = random.randint(1, 100)
Faça um programa que sorteia um número aleatório entre 1 e 100. Ele deve pedir para o usuário adivinhar o número até que ele acerte.

Quando o usuário finalmente acertar, exiba a mensagem "Você venceu!" e pergunte se ele gostaria de jogar novamente. Caso ele digite "sim", sorteie um novo número e torne a pedir que ele adivinhe.
'''

import random

print('=-' * 10)

print('JOGO DA ADIVINHAÇÃO')

print('=-' * 10)

max = 100

sorteio = random.randint(1, max)

resposta = 1

while resposta == 1:

    numero = int(input('Qual número você acha que o computador sorteou? '))

    while numero != sorteio:

        print('ERROU. Tente novamente!')

        if numero > sorteio:

            print('DICA: o número sorteado é MENOR que esse.')

        else:

            print('DICA: o número sorteado é MAIOR que esse.')

        numero = int(input('Qual número você acha que o computador sorteou? '))

    print(f'ACERTOU! O número sorteado foi o {sorteio} :)')

    print('''Deseja jogar novamente:
    
[0] Não

[1] Sim ''')

    resposta = int(input('Qual sua opção? '))

    sorteio = random.randint(1, max)

print('=-' * 10)

print('FIM DO JOGO')

print('=-' * 10)
