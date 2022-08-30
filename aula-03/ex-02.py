# Modifique o programa anterior para, além de ler o valor final pelo teclado, ler também o valor inicial.

numero_inicial = int(input('Informe o número (inteiro positivo) inicial da lista: '))

numero_final = int(input('Informe o número (inteiro positivo) final da lista: '))

while numero_inicial <= 0 or numero_final <= 0:

    print('ERRO! Os dois números devem ser inteiros positivos.')

    numero_inicial = int(input('Informe novamente o número inicial: '))

    numero_final = int(input('Informe novamente o número final: '))

while numero_inicial > numero_final:

    print('ERRO! O número inicial é maior que o número final.')

    numero_inicial = int(input('Informe novamente o número inicial: '))

    numero_final = int(input('Informe novamente o número final: '))

while numero_inicial <= numero_final:

    print(numero_inicial)

    numero_inicial += 1
