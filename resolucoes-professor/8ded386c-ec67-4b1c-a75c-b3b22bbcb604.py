tensao = float(input('Digite o valor da tensão: '))
r1 = float(input('Digite o valor do resistor R1: '))
r2 = float(input('Digite o valor do resistor R2: '))

req = (r1*r2)/(r1+r2)

i = tensao/req

print('Resistência equivalente: ', req)
print('Corrente: ', i)
