import random

sorteio = random.randint(0, 2)

opcoes = ['pedra', 'tesoura', 'papel']

jogada_computador = opcoes[sorteio]

jogada_humano = input('Escolha sua jogada (pedra, tesoura ou papel): ')

print('Computador jogou', jogada_computador)

if jogada_humano == jogada_computador:
    print('Empate!')

elif jogada_humano == 'pedra' and jogada_computador == 'tesoura' or jogada_humano == 'tesoura' and jogada_computador == 'papel' or jogada_humano == 'papel' and jogada_computador == 'pedra':
    print('Você venceu!')

else:
    print('Você perdeu!')
