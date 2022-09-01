'''
Faça um programa que pergunta a quantidade de provas realizadas pela usuária.
O seu programa deverá ler as notas das provas pelo teclado e responder:
- a média das provas
- a maior nota
- a menor nota
'''

num_provas = int(input('Informe o número de provas realizadas: '))

print('-' * 22)

soma = maior = menor = 0
for i in range(num_provas):
    nota = float(input(f'Nota da {i+1}ª prova: '))
    soma += nota
    if i == 0:
        maior = menor = nota
    else:
        if nota > maior:
            maior = nota
        elif nota < menor:
            menor = nota

print('-' * 22)

print(f'A média das suas notas nas {num_provas} provas é {(soma / num_provas):.1f}.\nA menor nota foi {menor:.1f} e a maior foi {maior:.1f}.')
