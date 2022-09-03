'''
Faça um programa que leia as coordenadas de dois vetores a partir do teclado e armazene-as em listas. Exemplo:

vetor1 = [1, 4, 7]
vetor2 = [2, 3, 4]
O seu programa deverá realizar a soma vetorial. No exemplo acima, ela é dada por:

soma = [1+2, 4+3, 7+4] = [3, 7, 11]
Dica: note que os valores a serem somados entre si possuem o mesmo índice em listas diferentes.
'''

n = int(input('Qual o tamanho dos dois vetores? '))

vetor1 = []
vetor2 = []
for i in range(n):
    vetor1.append(int(input(f'{i + 1}ª coordenada do vetor 1: ')))
    vetor2.append(int(input(f'{i + 1}ª coordenada do vetor 2: ')))

print('Vetor 1:', vetor1)
print('Vetor 2:', vetor2)

vetor_soma = []
for i in range(n):
    for j in range(n):
        if i == j:
            vetor_soma.append(vetor1[i] + vetor2[j])

print('Soma vetorial:', vetor_soma)
'''
# OUTRO MODO

zipada = list(zip(vetor1, vetor2))
somada = []
for pair in zipada:
    somada.append(sum(pair))
print(somada)
'''
