
print('=' * 115)
print('{:^115}'.format(' CÁLCULO DA RAIZ QUADRADA PELO MÉTODO DA BISSECÇÃO '))
print('=' * 115)

# número positivo - VERIFICAR SE É FLOAT
numero = float(input('Informe um número positivo: '))
while numero < 0:
    print('Opção inválida! Responda novamente:')
    numero = float(input('Informe um número positivo: '))

precisao = float(input('Informe a precisão que considera aceitável para o cálculo: '))

i = 0
f = 1000
while (f - i) > precisao:
    m = (i + f) / 2
    if m ** 2 > numero:
        f = m
    else:
         i = m

print(f'A raiz quadrada do número {numero}, calculada pelo método da bissecção considerando a precisão de {precisao}, é {m:.4f}.')

print('{:=^115}'.format(' FIM DO PROGRAMA '))

# VERIFICAR VALOR INICIAL f
# print(m)
# print(numero**(1/2))