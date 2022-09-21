
# Pedra quebra a tesoura
# Tesoura corta o papel
# Papel embrulha a pedra

from random import randint

print('{:*^60}'.format(' JOGO JOKENPO '))

jogador = input('Digite sua opção [pedra, tesoura ou papel]: ').strip().lower()

while jogador != 'pedra' and jogador != 'tesoura' and jogador != 'papel':
    print('\033[0;31mOpção inválida! Responda novamente:\033[m')
    jogador = input('Digite sua opção [pedra, tesoura ou papel]: ').strip().lower()

computador = randint(0, 2)  # pedra = 0, tesoura = 1, papel = 2

print(f'O coputador jogou ', end='')
if computador == 0:
    print('pedra.')
elif computador == 1:
    print('tesoura.')
else:
    print('papel.')

if jogador == 'pedra':
    if computador == 0:
        print('Empate!')
    elif computador == 1:
        print('Pedra quebra a tesoura. Você venceu!')
    else:
        print('Papel embrulha a pedra. Você perdeu!')
elif jogador == 'tesoura':
    if computador == 0:
        print('Pedra quebra a tesoura. Você perdeu!')
    elif computador == 1:
        print('Empate!')
    else:
        print('Tesoura corta o papel. Você venceu!')
else:
    if computador == 0:
        print('Papel embrulha a pedra. Você venceu!')
    elif computador == 1:
        print('Tesoura corta o papel. Você perdeu!')
    else:
        print('Empate!')

print('{:*^60}'.format(' FIM DO JOGO '))

# jogador = input('''Opções:
# [1] Pedra
# [2] Tesoura
# [3] Papel
# Informe a sua escolha: ''')




