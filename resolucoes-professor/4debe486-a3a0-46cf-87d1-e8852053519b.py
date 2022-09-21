numero = float(input('Digite o número para calcular a raiz quadrada: '))
erro = float(input('Digite a precisão: '))

inicio = 0
fim = numero

while fim - inicio > erro:
    meio = (fim + inicio) / 2

    if meio**2 > numero:
        fim = meio
    else:
        inicio = meio

print('Raiz quadrada:', meio)
