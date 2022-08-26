'''
Vamos fazer um programa para calcular o rendimento de uma aplicação.

Faça um programa que pergunta quanto dinheiro a usuária irá aplicar, a taxa de juros ao mês (em %) e a duração da aplicação (em meses).

Seu programa deve responder as seguintes informações:

Qual o valor total a ser sacado pela usuária ao final da aplicação?
Quantos reais a pessoa recebeu apenas de juros?
Quantos % a aplicação rendeu no total?
Atenção: ao buscar as fórmulas para utilizar no problema, busque pela fórmula de juros compostos. Não utilize a fórmula de juros simples.
'''

valor_aplicacao = float(input('Qual valor irá aplicar? R$ '))
taxa_juros = float(input('Qual a taxa de juros ao mês (em %)? '))
tempo = int(input('Por quantos meses irá aplicar? '))

valor_total = valor_aplicacao * (1 + taxa_juros / 100) ** tempo
valor_juros = valor_total - valor_aplicacao
rendimento_total = valor_juros * 100 / valor_aplicacao

print(f'O valor total a ser sacado ao final da aplicação é de R$ {valor_total:.2f}.')
print(f'O valor recebido apenas dos juros é de R$ {valor_juros:.2f}.')
print(f'No total, a aplicação rendeu {rendimento_total:.2f} %.')
