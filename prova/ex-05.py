
print('=-' * 30)

num_alunas = int(input('Quantas alunas o professor tem? '))

notas = []
for n in range(num_alunas):
    nota = float(input(f'Nota da {n+1}ª aluna: '))
    notas.append(nota)

soma = 0
for nota in notas:
    soma += nota

media = soma / num_alunas

somatorio = 0
for nota in notas:
    num = (nota - media)**2
    somatorio += num

variancia = somatorio / (num_alunas - 1)

print(f'A média das notas da turma é {media:.2f} e a variância é {variancia:.2f}.')

print('=-' * 30)

# print('Lista de notas:', notas)
# print(soma)
# print(sum(notas))

# print(media)
# print(sum(notas)/len(notas))

# print('Somatório:', somatorio)
# print(num_alunas, ' - ', len(notas))
