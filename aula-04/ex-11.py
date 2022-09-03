'''
Vamos implementar uma Tabela Price.

A tabela Price é utilizada em empréstimos de longo prazo, como no financiamento de um imóvel.

Um empréstimo pelo sistema Price utiliza prestações com valor fixo, isto é, você sempre irá pagar o mesmo valor todo mês.

Porém, uma taxa de juros corrige o seu saldo devedor, sendo assim, parte do valor que você paga no mês serve apenas para pagar juros, e outra parte realmente reduz o seu sald devedor. Essa redução é a chamada amortização.

Como o saldo devedor diminui com o tempo, a parcela de juros diminui a cada mês, nos primeiros meses a maior parte do valor pago por mês serve para pagar juros, enquanto mais próximo do final, a maior parte do valor está de fato amortizando a dívida.

Você pode aprender mais sobre as colunas da tabela e o cálculo para determinar o valor das prestações neste site.

Conhecendo o valor fixo, como fazemos para determinar quanto de amortização, quanto de juros e qual o novo saldo devedor a cada mês?

Primeiro aplica-se a taxa de juros sobre o saldo devedor (multiplicar por i). Esse valor é o valor de juros pagos no mês. Subtraindo-se os juros do valor da prestação, descobre-se o quanto se amortizou naquele mês. O novo saldo devedor é obtido subtraindo a amortização do valor.

Faça um programa que pergunta:

- o valor de um empréstimo
- a taxa de juros do empréstimo
- o tempo para pagamento

O seu programa deverá imprimir na tela uma "tabela" mostrando, mês a mês, o saldo devedor, juros, amortização e o valor da prestação.
'''

print('\033[1;33m*' * 20, 'TABELA PRICE', '*' * 20, '\033[m')

valor_emprestimo = float(input('Informe o valor do empéstimo: '))
taxa_juros = float(input('Informe o valor da taxa de juros (em %) do empréstimo: ')) / 100
tempo_pagamento = int(input('Informe o tempo (em meses) para pagamento: '))  # número de parcelas

n = (1 + taxa_juros)**tempo_pagamento
prestacao = valor_emprestimo * ((n * taxa_juros) / (n - 1))  # valor fixo a ser pago por mês

print('\033[1;33m-\033[m' * 54)

# print('Mês | Prestação (R$) | Juros (R$) | Amortização (R$) | Saldo devedor (R$)')

print('Mês | Prestação     | Juros         | Amortização   | Saldo devedor')

saldo_devedor = valor_emprestimo

for i in range(tempo_pagamento):

    juros = saldo_devedor * taxa_juros
    amortizacao = prestacao - juros
    saldo_devedor -= amortizacao

    print(f'{(i+1):^3} | R$ {prestacao:>10.2f} | R$ {juros:<10.2f} | R$ {amortizacao:<10.2f} | R$ {saldo_devedor:<10.2f}')

print('\033[1;33m-\033[m' * 54)
