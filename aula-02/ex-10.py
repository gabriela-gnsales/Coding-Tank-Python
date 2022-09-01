'''
Faça um programa que pergunta um ano para a usuária e responde se ele é bissexto ou não.

A regra geral para determinar se um ano é bissexto é: todo ano divisível por 4, a princípio, é bissexto: 2016, 2020, 2024...

Porém existe uma exceção: anos divisíveis por 100 não são bissextos. O ano 2100, por exemplo, é divisível por 4, mas como também é divisível por 100, ele não pode ser bissexto.

A exceção possui uma exceção: anos divisíveis por 400 são bissextos. O ano 2000, por exemplo, é divisível por 100. Porém, como ele também é divisível por 400, ele torna-se bissexto.
'''

ano = int(input('Informe um ano qualquer: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:

    print('Esse ano é BISSEXTO!')

else:

    print('Esse ano NÃO é BISSEXTO!')

# print('ano / 4 = ', (ano / 4))
# print('ano % 4 = ', (ano % 4))
#
# print('ano / 100 = ', ano / 100)
# print('ano % 100 = ', ano % 100)
#
# print('ano / 400 = ', (ano / 400))
# print('ano % 400 = ', (ano % 400))

'''
if (ano % 4) != 0:
    print('Esse ano NÃO é bissexto!')
elif (ano % 4) == 0 and (ano % 100) == 0:
    if (ano % 400) == 0:
        print('Esse ano é bissexto!')
    else:
        print('Esse ano NÃO é bissexto!')
# elif (ano % 4) == 0 and (ano % 100) != 0:
#     print('Esse ano é bissexto!')
else:
    print('Esse ano é bissexto!')
'''
