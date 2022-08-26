# Faça um programa que pergunta a nota das 4 provas de uma aluna e responde a sua média.

nota1 = float(input('Qual a sua nota na 1ª prova? '))
nota2 = float(input('Qual a sua nota na 2ª prova? '))
nota3 = float(input('Qual a sua nota na 3ª prova? '))
nota4 = float(input('Qual a sua nota na 4ª prova? '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'A média das suas notas nas quatro provas é {media:.1f}.')
