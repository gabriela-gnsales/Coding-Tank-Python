'''
Um banco oferece as seguintes opções de aplicação de renda fixa:

Fundo A: aceita aplicações a partir de 50 reais, não possui tempo mínimo de aplicação e rende 10% ao ano.

Fundo B: aceita aplicações a partir de 100 reais, possui tempo mínimo de aplicação de 1 ano e rende 12% ao ano.

Fundo C: aceita aplicações a partir de 500 reais, possui tempo mínimo de aplicação de 2 anos e rende 13% ao ano.

Fundo D: aceita aplicações a partir de 1000 reais, possui tempo mínimo de aplicação de 3 anos e rende 15% ao ano.

Fundo E: aceita aplicações a partir de 3000 reais, possui tempo mínimo de aplicação de 5 anos e rende 18% ao ano.

Faça um programa que pergunta para a usuária em qual fundo ela deseja aplicar seu dinheiro, quanto dinheiro ela possui e o tempo que ela pretende deixar o dinheiro aplicado (em anos).

Caso o valor e o tempo estejam adequados às regras do fundo selecionado, utilize a fórmula dos juros compostos para informar para ela o valor total que ela irá sacar ao final do período informado por ela.

Caso contrário, exiba a mensagem Não é possível realizar essa aplicação.
'''

fundo = input('Em qual fundo de renda fixa você deseja aplicar seu dinheiro (A, B, C, D ou E)? ').upper()

if fundo != 'A' and fundo != 'B' and fundo != 'C' and fundo != 'D' and fundo != 'E':
    print('Opção inválida.')
else:
    dinheiro = float(input('Quanto dinheiro você possui? R$ '))
    tempo_aplicacao = int(input('Por quantos anos deseja aplicar esse dinheiro? '))

    if fundo == 'A':
        if dinheiro >= 50 and tempo_aplicacao >= 0:
            valor_total = dinheiro * (1 + 10 / 100) ** tempo_aplicacao
            print(f'O valor total a ser sacado ao final da aplicação é de R$ {valor_total:.02f}.')
        else:
            print('Não é possível realizar essa aplicação.')
    elif fundo == 'B':
        if dinheiro >= 100 and tempo_aplicacao >= 1:
            valor_total = dinheiro * (1 + 12 / 100) ** tempo_aplicacao
            print(f'O valor total a ser sacado ao final da aplicação é de R$ {valor_total:.02f}.')
        else:
            print('Não é possível realizar essa aplicação.')
    elif fundo == 'C':
        if dinheiro >= 500 and tempo_aplicacao >= 2:
            valor_total = dinheiro * (1 + 13 / 100) ** tempo_aplicacao
            print(f'O valor total a ser sacado ao final da aplicação é de R$ {valor_total:.02f}.')
        else:
            print('Não é possível realizar essa aplicação.')
    elif fundo == 'D':
        if dinheiro >= 1000 and tempo_aplicacao >= 3:
            valor_total = dinheiro * (1 + 15 / 100) ** tempo_aplicacao
            print(f'O valor total a ser sacado ao final da aplicação é de R$ {valor_total:.02f}.')
        else:
            print('Não é possível realizar essa aplicação.')
    # elif fundo == 'E':
    else:
        if dinheiro >= 3000 and tempo_aplicacao >= 5:
            valor_total = dinheiro * (1 + 18 / 100) ** tempo_aplicacao
            print(f'O valor total a ser sacado ao final da aplicação é de R$ {valor_total:.02f}.')
        else:
            print('Não é possível realizar essa aplicação.')

# else:
#
#     print('Opção inválida.')

'''
fundo_a = fundo == 'A' and aplicacao >= 50 and tempo >= 0

fundo_b = fundo == 'B' and aplicacao >= 100 and tempo >= 1

fundo_c = fundo == 'C' and aplicacao >= 500 and tempo >= 2

fundo_d = fundo == 'D' and aplicacao >= 1000 and tempo >= 3

fundo_e = fundo == 'E' and aplicacao >= 3000 and tempo >= 5

if fundo_a or fundo_b or fundo_c or fundo_d or fundo_e:

if fundo_a:

    juros = 0.1

elif fundo_b:

    juros = 0.12

elif fundo_c:

    juros = 0.13

elif fundo_d:

    juros = 0.15

else:

    juros = 0.18
'''