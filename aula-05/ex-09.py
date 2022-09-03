'''
Crie uma tabela de preços (pode ser fixa no seu código) usando lista de listas.

Ela pode ser implementada da seguinte maneira: cada "lista interna" é uma lista de 2 elementos: na posição 0 temos o nome do produto, na posição 1 temos o preço.

Ex:

produtos = [
    ['Chocolate', 5.12],
    ['Doritos', 15.25],
    ['Fandangos', 7.54],
]
Faça um programa que permita consultar valores na lista.

Ele deverá perguntar para a usuária o nome do produto que ela deseja consultar. Caso o produto exista na lista, seu preço será exibido. Caso contrário, a mensagem "produto não encontrado" será exibida.

O programa deverá repetir a pergunta após mostrar o resultado, até que a usuária digite "sair".
'''

produtos = [
    ['Chocolate', 5.12],
    ['Doritos', 15.25],
    ['Fandangos', 7.54],
]

print('*' * 40, 'INÍCIO DA CONSULTA', '*' * 40)

print('-' * 25)
print(f'Produto    | Preço')
print('-' * 25)
print(f'{produtos[0][0]:10} | R$ {produtos[0][1]:>5}')
print(f'{produtos[1][0]:10} | R$ {produtos[1][1]:>5}')
print(f'{produtos[2][0]:10} | R$ {produtos[2][1]:>5}')
print('-' * 25)

while True:
    produto_consulta = input("Qual o nome do produto que deseja consultar o preço (para finalizar a consulta escreva 'sair')? ").strip().capitalize()

    if produto_consulta == 'Sair':
        break

    c = 0
    for produto in produtos:
        if produto_consulta == produto[0]:
            print(f'O preço do produto {produto[0].lower()} é R$ {produto[1]}.')
        else:
            c += 1
        if c == len(produtos):
            print('Produto não encontrado!')

print('*' * 40, 'FIM DA CONSULTA', '*' * 40)
