'''
Faça um programa que pergunta quantas provas a usuária fez. Em seguida, o programa deverá utilizar um laço for para ler cada uma de suas notas pelo teclado e informar sua média.
'''

num_provas = int(input('Quantas provas você fez? '))

soma = 0
for i in range(1, num_provas+1):
    nota = float(input(f'Nota da {i}ª prova: '))
    soma += nota

print(f'A média das suas notas nas {num_provas} provas é {(soma / num_provas):.1f}.')
