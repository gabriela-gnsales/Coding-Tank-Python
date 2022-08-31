'''
Iremos novamente fazer o programa da média do exercício anterior, mas com uma diferença: agora não iremos perguntar a quantidade de notas. A usuária deverá digitar uma nota negativa quando desejar parar de digitar mais notas.

Atenção: o número negativo não deve ser considerado uma nota (portanto, não deve interferir na média).
'''

nota = 1

i = 1

soma_notas = 0

while nota >= 0:

    nota = float(input(f'Informe a nota da {i}ª prova (para sair digite um valor negativo): '))

    if nota >= 0:

        soma_notas += nota

        i += 1

media_notas = soma_notas / (i - 1)

print(f'A média das suas notas nas {i - 1} provas é {media_notas:.1f}.')
