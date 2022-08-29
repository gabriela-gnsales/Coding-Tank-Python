'''
Modifique o programa das médias do exercício anterior da seguinte maneira:

Caso a aluna tenha ficado de exame, pergunte a nota do exame.

Uma nova média deve ser calculada entre a média original e a nota do exame:

media_exame = (media + exame)/2

O programa deve exibir essa nova média junto do novo status:

- Aprovada por exame caso a media_exame seja pelo menos 50.
- Reprovada caso a media_exame seja inferior a 50.
'''

nota1 = float(input('Qual a sua 1ª nota? '))

nota2 = float(input('Qual a sua 2ª nota? '))

media = (nota1 + nota2) / 2

print(f'A média das suas duas notas é {media:.1f}.')

if media >= 70:

    print('Parabéns, você está APROVADA!')

elif 30 <= media < 70:

    print('Você ficou de EXAME, estude mais um pouco!')

    exame = float(input('Qual a sua nota no exame? '))

    media_exame = (media + exame) / 2

    if media_exame >= 50:

        print(f'A nova média das suas notas, considerando o exame, é {media_exame}. Parabéns, você foi APROVADA!')

    else:

        print(f'A nova média das suas notas, considerando o exame, é {media_exame}. Infelizmente, você está REPROVADA!')

else:

    print('Infelizmente, você está REPROVADA!')
