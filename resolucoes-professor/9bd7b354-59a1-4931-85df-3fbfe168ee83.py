valor = float(input('Digite o valor a ser aplicado: '))
juros = float(input('Digite a taxa de juros da aplicação: '))
tempo = int(input('Digite o tempo de aplicação: '))

mes = 1
while mes <= tempo:
    rendimento = valor * juros/100
    valor = valor + rendimento
    print(f'Mês {mes} | Juros: {rendimento:.2f} reais, saldo: {valor:.2f} reais')
    mes = mes + 1

'''
Por que valor * juros ao invés de valor*(1+juros)**tempo?

Vamos pensar em como funcionam os tais dos juros compostos.
Considere o valor de 10000,00 reais aplicado a 5% de juros.
Ao final do primeiro mês, ele precisa render 5%.
Isso ocorre da seguinte maneira:
valor = 10000.0
juros = 0.05
rendimento = juros * valor # isso dá 500.0

Precisamos, em seguida, atualizar nosso total:
valor = valor + rendimento # isso dá 10500.0

Note que a fórmula para descobrir o valor atual é o valor "antigo" + rendimento.
Mas o rendimento é valor * juros. Substituindo:
valor = valor + valor * juros

Isso pode ser reescrito como:

valor = valor * (1 + juros) # familiar?

Note que no próximo mês repetiremos o procedimento todo.
Para descobrir o valor após 2 meses, teríamos:
valor = valor *(1 + juros)*(1 + juros) = valor*(1 + juros)**2

Após 3 meses, seria:
valor = valor*(1 + juros)*(1 + juros)*(1 + juros) = valor*(1 + juros)**3

E assim sucessivamente...

Ou seja, a famosa fórmula com o tempo no expoente é só o jeito "automático"
de descobrir os juros após "t" meses, ao invés de calcular passo-a-passo.

Porém, como neste exercício precisamos calcular mês-a-mês o rendimento e o
saldo, essa fórmula acaba sendo redundante. Acaba sendo "mais fácil"
calcular os juros do mês, atualizar o capital utilizando esses juros
e já exibir as duas informações na tela.

Muita gente (quase todas, na verdade) conseguiu fazer os cálculos corretamente
utilizando a fórmula completa, e isso não afetou a nota de ninguém :)
Você apenas acaba botando o computador para fazer bastante conta repetida sem motivo.
'''
