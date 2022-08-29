'''
Faça um programa que pergunta o nome da usuária e o horário do dia (apenas horas, sem os minutos). O programa deverá responder:

- Bom dia, [nome]! caso o horário esteja entre 4 e 11.
- Boa tarde, [nome]! caso o horário esteja entre 12 e 17.
- Boa noite, [nome]! caso o horário esteja entre 18 e 23 ou 0 e 3.
- Horário inválido caso o horário seja superior a 23 ou inferior a 0.
'''

nome = input('Qual o seu nome? ')

horario = int(input('Qual o horário agora? '))

if 4 <= horario <= 11:

    print(f'Bom dia, {nome}!')

elif 12 <= horario <= 17:

    print(f'Boa tarde, {nome}!')

elif 18 <= horario <= 23 or 0 <= horario <= 3:

    print(f'Boa noite, {nome}!')

else:

    print('Horário inválido.')
