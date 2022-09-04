'''
Nesta questão, reaproveite o código da questão avaliada da lista de exercícios anterior!

Modifique seu código para, ao invés de exibir a tabela Price na tela, armazenar a tabela utilizando uma lista de listas.

Cada "lista interna" deve conter juros daquele mês, amortização daquele mês, valor da prestação e saldo devedor.

Todas essas listas deverão ser adicionadas, na ordem correta, em uma lista geral, que será nossa tabela.

Uma vez criada e calculada toda a tabela, pergunte (em loop) para a usuária qual mês ela deseja consultar e mostre para ela quanto de juros serão pagos, quanto será amortizado e qual será o seu saldo devedor naquele mês. Caso ela digite um mês inválido, informe para ela que aquele mês não existe. Caso ela digite um mês negativo, encerre o programa.
'''

print('\033[1;33m*' * 28, 'TABELA PRICE', '*' * 28, '\033[m')

valor_emprestimo = float(input('Informe o valor do empréstimo: '))
taxa_juros = float(input('Informe o valor da taxa de juros (em %) do empréstimo: ')) / 100
tempo_pagamento = int(input('Informe o tempo (em meses) para pagamento: '))  # número de parcelas

n = (1 + taxa_juros)**tempo_pagamento
prestacao = valor_emprestimo * ((n * taxa_juros) / (n - 1))  # valor fixo a ser pago por mês

print('\033[1;33m-\033[m' * 70)

# print('\033[1;32mMês\033[m | \033[1;32mPrestação\033[m     | \033[1;32mJuros\033[m         | \033[1;32mAmortização\033[m   | \033[1;32mSaldo devedor\033[m')

saldo_devedor = valor_emprestimo

lista_juros = []
lista_amortizacao = []
lista_saldo_devedor = []
lista = []

for i in range(tempo_pagamento):

    juros = saldo_devedor * taxa_juros
    lista_juros.append(juros)

    amortizacao = prestacao - juros
    lista_amortizacao.append(amortizacao)

    saldo_devedor -= amortizacao
    lista_saldo_devedor.append(saldo_devedor)

    for j in range(5):
        lista[0] = lista.append(prestacao)
        lista[1] = lista.append(juros)
        lista[2] = lista.append(amortizacao)
        lista[3] = lista.append(saldo_devedor)

    # print(f'{(i+1):^3} | R$ {prestacao:^10.2f} | R$ {juros:^10.2f} | R$ {amortizacao:^10.2f} | R$ {saldo_devedor:^10.2f}')

print(f'Lista:', lista)

# print(f'Lista juros:', lista_juros)
# print('Lista amortizacao:', lista_amortizacao)
# print('Lista saldo devedor:', lista_saldo_devedor)



print('\033[1;33m-\033[m' * 70)
