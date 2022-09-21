#### Dados de entrada: valor inicial, taxa de juros, tempo

valor_inicial = float(input('Digite o valor a ser aplicado: '))
juros = float(input('Digite a taxa de juros da aplicação: '))
tempo = float(input('Digite a duração da aplicação: '))

#### Processamento

# Valor final: vem da fórmula de juros compostos: M = *C(1+i)**t
# M = montante, C = capital inicial, i = taxa de juros, t = tempo
# Mas juros (i) deve ser um número entre 0 e 1.
# Logo, dividiremos nossos juros (que estão em porcento) por 100.
valor_final = valor_inicial * (1 + juros/100) ** tempo

# Rendimento: é a diferença entre o que aplicamos e o que sacaremos
rendimento = valor_final - valor_inicial

# Rendimento percentual: relação entre o que rendeu e o que aplicamos
# Também dá um número de 0 a 1, por isso multiplicamos por 100 pra chegar em %
rendimento_porcento = (rendimento/valor_inicial) * 100
# outra fórmula que muita gente usou e é equivalente (ver explicação lá embaixo):
# rendimento_porcento = (valor_final/valor_inicial)*100 - 100

#### Saída (valor a sacar, ganhos e percentual de rendimento):
print('Valor a sacar: R$', valor_final)
print('Ganhos com juros: R$', rendimento)
print('A aplicação rendeu', rendimento_porcento, '% no período')


'''
Por que as duas fórmulas são iguais?

Vamos começar igualando as duas:
(rendimento/valor_inicial)*100 = (valor_final/valor_inicial)*100 - 100

Lembre-se que rendimento = valor_final - valor_inicial, portanto:
(valor_final-valor_inicial)/(valor_inicial) * 100 = (valor_final/valor_inicial)*100 - 100

Aplicando a propriedade distributiva no lado esquerdo da igualdade:
(valor_final/valor_inicial)*100 - (valor_inicial/valor_inicial)*100 = (valor_final/valor_inicial)*100 - 100

Um número dividido por ele mesmo é igual a 1:
(valor_final/valor_inicial)*100 - (1)*100 = (valor_final/valor_inicial)*100 - 100

Portanto:
(valor_final/valor_inicial)*100 - 100 = (valor_final/valor_inicial)*100 - 100
'''





