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
