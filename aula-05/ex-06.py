'''
Faça um programa que pergunta o número de atividades avaliativas realizadas pela usuária (no mínimo 4).

O programa deverá exibir:
- a menor nota
- a maior nota
- a média calculada desconsiderando a maior e a menor nota
'''

num_avaliacoes = int(input('Qual o número de atividades avaliativas realizadas? '))

while num_avaliacoes < 4:
    num_avaliacoes = int(input('Informe, no mínimo, 4 atividades avaliativas: '))

notas = []

for nota in range(num_avaliacoes):
    nota = float(input(f'Nota da {nota+1}ª avaliação: '))
    notas.append(nota)
print(f'Lista das notas das {num_avaliacoes} avaliações: {notas}')

media = sum(notas) / num_avaliacoes
menor = min(notas)
maior = max(notas)
print(f'A média das {num_avaliacoes} notas é {media:.1f}.\nA menor nota foi {menor} e a maior foi {maior}.')

notas.remove(maior)
notas.remove(menor)
print('Lista sem as notas maior e menor:', notas)

media = sum(notas) / len(notas)
print(f'A média calculada desconsiderando a maior e a menor nota é {media:.1f}')
