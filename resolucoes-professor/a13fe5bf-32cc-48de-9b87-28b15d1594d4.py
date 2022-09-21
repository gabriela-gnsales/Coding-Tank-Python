# Código dado:

'''
for x in range(1, 30):
    if x % 2 == 0 and x % 10 == 0:
        comando1
    if x % 3 == 0 and x % 4 == 0:
        comando2
    if x % 3 == 0 and x % 11 == 0:
        comando3
'''

# Resolvendo por lógica:
# O valor de 'x' varia de 1 em 1, começando em 1 e terminando em 29
# primeiro if:
## estamos testando resto de divisão de x por 2 e x por 10
## 10 satisfaz esse valor, 20 também
# segundo if:
## estamos testando resto de divisão de x por 3 e por 4
## 12 satisfaz esse valor, 24 também
# terceiro if:
## estamos testando resto de divisão de x por 3 e por 11
## primeiro valor que daria True seria 33, fora do nosso intervalo

# portanto, "comando3" não é executado

# resolvendo por código: troque cada comando por um "print" e execute:

for x in range(1, 30):
    if x % 2 == 0 and x % 10 == 0:
        print('x:', x, '| comando1')
    if x % 3 == 0 and x % 4 == 0:
        print('x:', x, '| comando2')
    if x % 3 == 0 and x % 11 == 0:
        print('x:', x, '| comando3')

# note que comando3 nunca executou
