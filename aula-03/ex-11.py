'''
Pergunte para a usuária o valor que será investido em uma aplicação, a taxa de juros ao mês e o tempo que o dinheiro ficará aplicado.

Seu programa deverá exibir quanto de juros será pago e o saldo total em cada mês.
'''

valor = float(input('Qual valor deseja aplicar? R$ '))

taxa_juros = float(input('Qual a taxa de juros ao mês (em %)? '))

tempo = int(input('Por quantos meses quer deixar seu dinheiro aplicado? '))

i = 1

print('=-' * 22)

while tempo > 0:

    saldo = valor * (1 + taxa_juros / 100) ** 1

    juros = saldo - valor

    print(f'Mês {i}: juros = R$ {juros:.02f} - saldo = R$ {saldo:.02f}')

    i += 1

    tempo -= 1

    valor = saldo

print('=-' * 22)
