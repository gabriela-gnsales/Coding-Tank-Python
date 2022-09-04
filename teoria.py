print('Hello, world!')

# comunidade python adota o padrão de nome de variável "snake_case": palavras separadas por underline, ex: nome_da_variavel

# python não adota pontuação no final do código / linha

# f string agora é usado no lugar de format

# pattern matching -> recurso pra ter o switch case

# off-by-one error

lista_vazia = []
lista_vazia2 = list()

print(lista_vazia)
print(lista_vazia2)

print(len(lista_vazia))
print(len(lista_vazia2))

lista = ['ola', 10, 5.2, True]
print(lista)
print(type(lista))
print(type(lista[0]))
print(type(lista[1]))
print(type(lista[2]))
print(type(lista[3]))
print(len(lista))

# usado só para ler dados, pq não dá para modificar os elementos da lista, só a cópia deles
for i in lista:
    print(i)

notas = [float(input('Nota: ')) for i in range(int(input('Quantidade: ')))]

print(notas)

for i in range(len(vetor1)):
    soma.append(vetor1[i] + vetor2[i])
print(soma)

#--------------------------------------

zipada = list(zip(vetor1, vetor2))
somada = []
for pair in zipada:
    somada.append(sum(pair))
print(somada)

#-------------------------------------

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
