'''
Faça um programa que pergunta quantas provas a usuária fez. Em seguida, o programa deverá ler cada uma de suas notas pelo teclado e informar sua média.
'''

num_provas = int(input('Quantas provas você fez? '))

soma_notas = 0

i = 1

while num_provas > 0:

    nota = float(input(f'Informe a nota da {i}ª prova: '))

    soma_notas += nota

    num_provas -= 1

    i += 1

media_notas = soma_notas / (i - 1)

print(f'A média das suas notas nas {i - 1} provas é {media_notas:.1f}.')
