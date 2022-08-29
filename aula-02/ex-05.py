'''
Faça um programa que deverá pedir as 2 notas de uma aluna e calcular sua média. Considere que as notas serão de 0 a 100.

O programa deverá informar a média da aluna e seu status, obedecendo as regrinhas abaixo:

- Aprovada, caso a média seja pelo menos 70.
- Exame, caso a média seja pelo menos 30 e menor do que 70.
- Reprovada caso a média seja inferior a 30.
'''

nota1 = float(input('Qual a sua 1ª nota? '))

nota2 = float(input('Qual a sua 2ª nota? '))

media = (nota1 + nota2) / 2

print(f'A média das suas duas notas é {media:.1f}.')

if media >= 70:

    print('Parabéns, você está APROVADA!')

elif 30 <= media < 70:

    print('Você ficou de EXAME, estude mais um pouco!')

else:

    print('Infelizmente, você está REPROVADA!')
