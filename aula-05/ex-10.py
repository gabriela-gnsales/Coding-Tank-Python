'''
Vamos fazer um programa para representar uma aluna em formato amigável para salvar em uma tabela ou banco de dados.

Peça para a usuária digitar:
- o nome da aluna
- o número de matrícula
- a quantidade de provas realizadas
- a nota de cada uma das provas
- o percentual de presenças

A aluna deverá ser representada em uma lista obedecendo a seguinte estrutura:
- índice 0: número de matrícula
- índice 1: nome
- índice 2: uma lista com todas as suas notas
- índice 3: sua média
- índice 4: seu percentual de presenças
- índice 5: um booleano indicando se a aluna foi aprovada ou reprovada

Considere como critério de aprovação nota maior ou igual a 6.0 e presença igual ou superior a 70%.
'''

print('*' * 40, 'CADASTRO DE ALUNOS', '*' * 40)

nome = input('Nome do aluno(a): ').strip().capitalize()
matricula = int(input('Numero da matrícula: '))
num_provas = int(input('Número de provas realizadas: '))

notas = []
for i in range(num_provas):
    notas.append(float(input(f'Nota da {i+1}ª prova: ')))

percentual_presencas = int(input('Percentual de presenças: '))

media = sum(notas)/len(notas)
if media >= 6 and percentual_presencas >= 70:
    status = True
else:
    status = False

print('*' * 100)
cadastro = [matricula, nome, notas, media, percentual_presencas, status]

print('Cadastro aluno(a): nº da matrícula, nome, lista de notas, média das notas, percentual de presença, status aprovação')
print('Cadastro aluno(a):', cadastro)
