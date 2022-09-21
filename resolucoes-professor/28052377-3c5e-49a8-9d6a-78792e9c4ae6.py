notas = []  

quantidade = int(input('Digite a quantidade de provas: '))

# lembrete: ainda não temos uma lista montada para PERCORRER
# portanto, vamos usar um loop que CONTA REPETIÇÕES
for contador in range(quantidade):
    nota = float(input('Digite a nota: '))
    notas.append(nota)

maior = max(notas)
menor = min(notas)

print('tamanho da lista: ', len(notas))
notas.remove(menor)
print('tamanho da lista depois da remoção: ', len(notas))
soma = 0
for nota in notas:
    soma = soma + nota
media = soma/len(notas)



print('Suas notas foram:', notas)
print('Sua média foi:', media)
print('Suas maior e menor nota, foram, respectivamente:', maior, menor)





'''
notas = [10.0, 9.0, 9.5, 9.5]
#indice=    0    1    2    3

print(notas[1])

print(notas[0])

notas[2] = 10.0

print(notas)

curso = ['Coding Tank', 6, 40, 'Python', True]

print(curso)

print(curso[0])

print(notas)

soma = 0
for indice in range(4):
    print('Posição:', indice, '| Valor:', notas[indice])
    soma = soma + notas[indice]

media = soma/4
print(media)


# tirando um ponto de todo mundo...
for indice in range(4):
    notas[indice] = notas[indice] - 1 # notas[indice]-=1
#print(notas[4])


# usando o for para percorrer uma lista DIRETAMENTE:
for elemento in notas:
    print('Nota:', elemento)


soma = 0
for elemento in notas:
    soma = soma + elemento
media = soma/4
print(media)


for elemento in notas:
    elemento = elemento + 1
    print('elemento atualizado:', elemento)
print(notas)
'''
