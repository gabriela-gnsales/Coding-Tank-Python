x = 10 >= 9
print(x)
y = 10 < 1000
print(y)

valor_aplicado = float(input("Qual é a quantidade de dinheiro que será investida? "))
taxa_juros = float(input("Qual é a taxa de juros da aplicação? "))
duracao_aplicacao_meses = int(input("Qual é a quantidade de meses que o dinheiro ficará alocado no fundo? "))
print("______________________________________________")

contador = 1
while contador <= duracao_aplicacao_meses:
    montante_mensal = valor_aplicado * (1 + (taxa_juros / 100)) ** 1
    print("Mês: ", contador, "Juros:  ", montante_mensa valor_aplicado = montante_mensal
    contador += 1
    print("___________________________________________")

total = 0
nota = 0
contador = 0
while nota >= 0:
    total += nota
    contador += 1
    nota = float(input("Digite a nota "))

print("A média é: ", total / (contador - 1))
