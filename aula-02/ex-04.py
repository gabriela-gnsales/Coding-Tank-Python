'''
Faça um programa que pergunta o nome e o gênero da pessoa que está utilizando. O programa deverá responder:

- Seja bem-vindo, [nome]! caso o gênero seja igual a 'M'
- Seja bem-vinda, [nome]! caso o gênero seja igual a 'F'
- Sej@ bem-vind@, [nome]! caso o gênero seja 'Neutro' ou 'Outro'
- Opção inválida caso gênero não possua um dos 3 valores descritos acima.
'''

nome = input('Qual o seu nome? ')

genero = input('Qual o seu gênero (M, F, Neutro ou Outro)? ').upper()

if genero == 'M':

    print(f'Seja bem-vindo, {nome}!')

elif genero == 'F':

    print(f'Seja bem-vinda, {nome}!')

elif genero == 'NEUTRO' or genero == 'OUTRO':

    print(f'Seja bem-vind@, {nome}!')

else:

    print('Opção inválida.')
