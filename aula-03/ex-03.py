# Modifique o programa anterior para perguntar também o "passo", ou seja, de quantas em quantas unidades a contagem irá saltar.

numero_inicial = int(input('Informe o número (inteiro positivo) inicial da lista: '))

numero_final = int(input('Informe o número (inteiro positivo) final da lista: '))

passo = int(input('Informe o "passo" (inteiro positivo), ou seja, de quantas em quantas unidades a contagem irá saltar: '))

while numero_inicial <= 0 or numero_final <= 0 or passo <= 0:

    print('ERRO! Os dois números devem ser inteiros positivos.')

    numero_inicial = int(input('Informe novamente o número inicial: '))

    numero_final = int(input('Informe novamente o número final: '))

    passo = int(input('Informe novamente o passo: '))

while numero_inicial > numero_final:

    print('ERRO! O número inicial é maior que o número final.')

    numero_inicial = int(input('Informe novamente o número inicial: '))

    numero_final = int(input('Informe novamente o número final: '))

while passo > numero_inicial - numero_final:

    print('ERRO! O passo não é um valor válido.')

    passo = int(input('Informe novamente o passo: '))

while numero_inicial <= numero_final:

    print(numero_inicial)

    numero_inicial += passo
