alunas = int(input('Digite o número de alunas: '))

notas = []
soma = 0

for contador in range(alunas):
    nota = float(input('Digite a nota: '))
    notas.append(nota)
    soma = soma + nota

media = soma/alunas

soma = 0

for nota in notas:
    soma = soma + (nota - media)**2

variancia = soma/(alunas-1)

print('Média:', media)
print('Variância:', variancia)
