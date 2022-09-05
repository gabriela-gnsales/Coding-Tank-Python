'''
Nesta questão, reaproveite o código da questão avaliada da lista de exercícios anterior!

Modifique seu código para, ao invés de exibir a tabela Price na tela, armazenar a tabela utilizando uma lista de listas.

Cada "lista interna" deve conter juros daquele mês, amortização daquele mês, valor da prestação e saldo devedor.

Todas essas listas deverão ser adicionadas, na ordem correta, em uma lista geral, que será nossa tabela.

Uma vez criada e calculada toda a tabela, pergunte (em loop) para a usuária qual mês ela deseja consultar e mostre para ela quanto de juros serão pagos, quanto será amortizado e qual será o seu saldo devedor naquele mês. Caso ela digite um mês inválido, informe para ela que aquele mês não existe. Caso ela digite um mês negativo, encerre o programa.
'''

# print('\033[1;33m{:*^80}\033[m'.format(' TABELA PRICE '))

print('\033[1;33m=' * 75)
print('{:^80}'.format('TABELA PRICE'))
print('\033[1;33m=\033[m' * 75)

# Solicitando os dados de entrada
valor_emprestimo = float(input('Informe o valor do empréstimo: '))
taxa_juros = float(input('Informe o valor da taxa de juros (em %) do empréstimo: ')) / 100
tempo_pagamento = int(input('Informe o tempo (em meses) para pagamento: '))  # número de parcelas

# Calculando o valor fixo a ser pago por mês (prestação mensal)
n = (1 + taxa_juros)**tempo_pagamento
prestacao = valor_emprestimo * ((n * taxa_juros) / (n - 1))

# Criando a lista com todos os valores mensais referentes ao empréstimo
emprestimo_total = list()
saldo_devedor = valor_emprestimo
for mes in range(tempo_pagamento):

    juros = saldo_devedor * taxa_juros
    amortizacao = prestacao - juros
    saldo_devedor -= amortizacao

    emprestimo_mensal = list()
    emprestimo_mensal.append(prestacao)
    emprestimo_mensal.append(juros)
    emprestimo_mensal.append(amortizacao)
    emprestimo_mensal.append(saldo_devedor)

    emprestimo_total.append(emprestimo_mensal)

print('\033[1;33m{:-^75}\033[m'.format(' Início da consulta '))

# Lendo a consulta da usuária
while True:
    mes = int(input('Qual mês deseja consultar [para encerrar digite um valor negativo]? '))

    while mes not in range(1, tempo_pagamento + 1) and mes >= 0:
        print('\033[0;31mEsse mês não existe. Responda novamente:\033[m')
        mes = int(input('Qual mês deseja consultar [para encerrar digite um valor negativo]? '))

    if mes < 0:
        break

    for m in range(len(emprestimo_total)):
        if m == (mes - 1):
            print('\033[1;32m-\033[m' * 28)
            print('\033[1;32m{:^30}\033[m'.format(f'MÊS {mes}'))
            print('{:14} {:.<2} {:>8.2f}'.format('Prestação:', 'R$', emprestimo_total[m][0]))
            print('{:14} {:<2} {:>8.2f}'.format('Juros:', 'R$', emprestimo_total[m][1]))
            print('{:14} {:<2} {:>8.2f}'.format('Amortização:', 'R$', emprestimo_total[m][2]))
            print('{:14} {:<2} {:>8.2f}'.format('Saldo devedor:', 'R$', emprestimo_total[m][3]))
            print('\033[1;32m-\033[m' * 28)

print('\033[1;33m{:-^75}\033[m'.format(' Fim da consulta '))
