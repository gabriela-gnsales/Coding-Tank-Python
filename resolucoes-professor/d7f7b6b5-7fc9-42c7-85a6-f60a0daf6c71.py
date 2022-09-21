print('Fundo A: valor mínimo: 50 reais, sem tempo mínimo, rende 10% ao ano.')
print('Fundo B: valor mínimo: 100 reais, tempo mínimo: 1 ano, rende 12% ao ano.')
print('Fundo C: valor mínimo: 500 reais, tempo mínimo: 2 anos, rende 13% ao ano.')
print('Fundo D: valor mínimo: 1000 reais, tempo mínimo: 3 anos, rende 15% ao ano.')
print('Fundo E: valor mínimo: 3000 reais, tempo mínimo: 5 anos, rende 18% ao ano.')

aplicacao = input('Escolha sua aplicação: ')
valor = float(input('Digite o valor para investir: '))
tempo = int(input('Digite a duração em anos da aplicação: '))

# Caso uma aplicação válida e com as regras atendidas seja selecionada, ajustamos seus juros
if aplicacao == 'A' and valor >= 50:
    juros = 1.1
elif aplicacao == 'B' and valor >= 100 and tempo >= 1:
    juros = 1.2
elif aplicacao == 'C' and valor >= 500 and tempo >= 2:
    juros = 1.3
elif aplicacao == 'D' and valor >= 1000 and tempo >= 3:
    juros = 1.5
elif aplicacao == 'E' and valor >= 3000 and tempo >= 5:
    juros = 1.8
# aplicação inválida ou regras desrespeitadas, zeramos o juro
else:
    juros = 0

# juros = 0 representa falha, > 0 representa sucesso e podemos fazer o cálculo
if juros > 0:
    montante = valor*(juros)**tempo
    print(f'Valor a sacar: R$ {montante:.2f}')
else:
    print('Não foi possível realizar a aplicação.')
