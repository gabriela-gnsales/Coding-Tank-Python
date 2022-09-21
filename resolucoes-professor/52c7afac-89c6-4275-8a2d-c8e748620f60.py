saldo = float(input('Digite o valor do empréstimo: '))
taxa = float(input('Digite a taxa de juros: '))
tempo = int(input('Digite o tempo do empréstimo: '))

taxa = taxa/100

amortizacao = saldo/tempo

for mes in range(1, tempo+1):
    juros = saldo * taxa
    prestacao = amortizacao + juros
    saldo = saldo - amortizacao
    print('Mês:', round(mes,2),
          '| Prestação:', round(prestacao,2),
          '| Juros:', round(juros,2),
          '| Amortização:', round(amortizacao,2),
          '| Saldo:', round(saldo, 2))
