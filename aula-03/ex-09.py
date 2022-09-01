'''
Faça um programa que pergunta o nome e o gênero da pessoa que está utilizando. O programa deverá responder:

- Seja bem-vindo, [nome]! caso o gênero seja igual a 'M'
- Seja bem-vinda, [nome]! caso o gênero seja igual a 'F'
- Sej@ bem-vind@, [nome]! caso o gênero seja 'Neutro' ou 'Outro'

Caso uma opção diferente das listadas acima seja digitada, o programa deverá repetir a pergunta até que uma das opções válidas seja digitada.
'''

nome = input('Qual o seu nome? ').strip().capitalize()

genero = input('Qual o seu gênero (M, F, Neutro ou Outro)? ').strip().lower()

while genero != 'm' and genero != 'f' and genero != 'neutro' and genero != 'outro':

    print('Opção de gênero inválida!')

    genero = input('Qual o seu gênero (M, F, Neutro ou Outro)? ').strip().lower()

if genero == 'm':

    print(f'Seja bem-vindo, {nome}!')

elif genero == 'f':

    print(f'Seja bem-vinda, {nome}!')

else:

    print(f'Seja bem-vind@, {nome}!')

'''
opcao = 1

while opcao == 1:

    if genero == 'm':

        print(f'Seja bem-vindo, {nome}!')

        break

    elif genero == 'f':

        print(f'Seja bem-vinda, {nome}!')

        break

    elif genero == 'neutro' or genero == 'outro':

        print(f'Seja bem-vind@, {nome}!')

        break

    else:

        opcao = 0

        while opcao == 0:

            print('Opção de gênero inválida!')

            genero = input('Qual o seu gênero (M, F, Neutro ou Outro)? ').lower()

            if genero == 'm' or genero == 'f' or genero == 'neutro' or genero == 'outro':

                opcao = 1
'''
