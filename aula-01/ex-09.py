'''
Vai um cupom de desconto aí?

Faça um programa que pergunta o preço de um produto, o desconto a ser aplicado (em %) e responde o valor total a ser pago.
'''
preco = float(input('Qual o preço do produto? R$ '))
desconto = float(input('Qual o desconto a ser aplicado (em %)? '))

novo_preco = preco - (preco * desconto / 100)

print(f'O valor total a ser pago é de R$ {novo_preco:.2f}.')
