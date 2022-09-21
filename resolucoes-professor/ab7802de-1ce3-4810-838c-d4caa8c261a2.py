saldo = float(input('Digite o valor do empréstimo: '))
taxa = float(input('Digite a taxa de juros: '))
tempo = int(input('Digite o tempo do empréstimo: '))

taxa = taxa/100

prestacao = saldo*((1+taxa)**tempo)*taxa/((1+taxa)**tempo - 1)

for mes in range(1, tempo+1):
    juros = saldo * taxa
    amortizacao = prestacao - juros
    saldo = saldo - amortizacao
    print('Mês:', round(mes,2),
          '| Prestação:', round(prestacao,2),
          '| Juros:', round(juros,2),
          '| Amortização:', round(amortizacao,2),
          '| Saldo:', round(saldo, 2))
