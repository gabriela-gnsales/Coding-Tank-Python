'''
Faça um programa que leia as coordenadas de dois vetores a partir do teclado e armazene-as em listas. Exemplo:

vetor1 = [1, 4, 7]
vetor2 = [2, 3, 4]
O seu programa deverá realizar o produto escalar. No exemplo acima, ele é dado por:

produto = 1*2 + 4*3 + 7*4 = 42
Atenção: note que o produto escalar, apesar de ser uma operação entre vetores, possui como resultado um único número.
'''

n = int(input('Qual o tamanho dos dois vetores? '))

vetor1 = []
vetor2 = []
for i in range(n):
    vetor1.append(int(input(f'{i + 1}ª coordenada do vetor 1: ')))
    vetor2.append(int(input(f'{i + 1}ª coordenada do vetor 2: ')))

print('Vetor 1:', vetor1)
print('Vetor 2:', vetor2)

soma = 0
for i in range(n):
    for j in range(n):
        if i == j:
            produto = vetor1[i] * vetor2[j]
            print(f'({vetor1[i]}x{vetor2[j]})', end='')
            if i == n-1:
                print(' = ', end='')
            else:
                print(' + ', end='')
            soma += produto
print(soma)
print('Produto escalar:', soma)
