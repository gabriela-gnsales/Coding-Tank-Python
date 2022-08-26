'''
Vamos falar de coisa boa: aumento salarial!

Faça um programa que pergunta o salário da funcionária, o aumento a ser aplicado (em %) e responde o seu novo salário.
'''
salario = float(input('Qual o seu salário? R$ '))
aumento = float(input('Qual o aumento a ser aplicado (em %)? '))

novo_salario = salario * (1 + aumento / 100)

print(f'O seu novo salário é de R$ {novo_salario:.2f}.')
