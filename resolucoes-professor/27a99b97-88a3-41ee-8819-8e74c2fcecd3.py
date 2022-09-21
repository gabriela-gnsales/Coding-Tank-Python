saldo = float(input('Digite o valor do empréstimo: '))
taxa = float(input('Digite a taxa de juros: '))
tempo = int(input('Digite o tempo do empréstimo: '))

taxa = taxa/100

prestacao = saldo*((1+taxa)**tempo)*taxa/((1+taxa)**tempo - 1)

tabela_price = []

for mes in range(1, tempo+1):
    juros = saldo * taxa
    amortizacao = prestacao - juros
    saldo = saldo - amortizacao
    tabela_price.append([round(mes,2), round(prestacao,2), round(juros,2), round(amortizacao,2), round(saldo, 2)])

mes = 0

while mes >= 0:
    mes = int(input('Digite o mês para consultar: '))

    if mes <= 0 or mes > tempo:
        print('Opção inválida!')

    else:
        print('Mês:', round(tabela_price[mes-1][0],2),
          '| Prestação:', round(tabela_price[mes-1][1],2),
          '| Juros:', round(tabela_price[mes-1][2],2),
          '| Amortização:', round(tabela_price[mes-1][3],2),
          '| Saldo:', round(tabela_price[mes-1][4], 2))

