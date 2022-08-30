'''
Modifique o programa dos triângulos do exercício anterior da seguinte maneira:

Caso o programa tenha determinado que o triângulo existe, informe também o seu tipo:

- Equilátero, caso os 3 lados sejam iguais
- Isósceles, caso apenas 2 lados sejam iguais
- Escaleno, caso todos os lados sejam diferentes entre si
'''

lado1 = float(input('Qual o comprimento do lado 1 do triângulo? '))

lado2 = float(input('Qual o comprimento do lado 2 do triângulo? '))

lado3 = float(input('Qual o comprimento do lado 3 do triângulo? '))

if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2):

    if lado1 == lado2 == lado3:  # lado1 == lado2 and lado1 == lado3:

        print('É um triângulo equilátero.')

    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:

        print('É um triângulo escaleno.')

    else:

        print('É um triângulo isósceles.')

else:

    print('Não é um triângulo!')

'''
dá pra fazer algo como:

if lado1 < lado2 + lado3 AND...: é triângulo

ou:

if lado1 >= lado2 + lado3 OR....: não é triângulo

Quando queremos inverter um "or", a gente inverte as duas afirmações e transforma o or em and, e vice-versa:

not(A or B) = (not A) and (not B)
not(A and B) = (not A) or (not B)
'''
