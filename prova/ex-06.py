
print('\033[1;33m=' * 70)
print('{:^70}'.format('TABELA SAC'))
print('\033[1;33m=\033[m' * 70)

# Solicitando os dados de entrada
valor_emprestimo = float(input('Informe o valor do empréstimo: '))
taxa_juros = float(input('Informe o valor da taxa de juros (em %) do empréstimo: ')) / 100
prazo_pagamento = int(input('Informe o prazo (em meses) para quitar o empréstimo: '))  # número de parcelas

print('\033[1;33m-\033[m' * 70)

print('\033[1;32m{:^5}\033[m | \033[1;32m{:^13}\033[m | \033[1;32m{:^13}\033[m | \033[1;32m{:^13}\033[m | \033[1;32m{:^13}\033[m'.format('Mês', 'Juros', 'Amortização', 'Prestação', 'Saldo devedor'))

# Calculando o valor fixo da amortização
saldo_devedor = valor_emprestimo
amortizacao = saldo_devedor / prazo_pagamento

for mes in range(prazo_pagamento):

    juros = saldo_devedor * taxa_juros
    prestacao = juros + amortizacao
    saldo_devedor -= amortizacao

    print(f'{(mes+1):^5} | R$ {juros:>10.2f} | R$ {amortizacao:>10.2f} | R$ {prestacao:>10.2f} | R$ {saldo_devedor:>10.2f}')

print('\033[1;33m-\033[m' * 70)
