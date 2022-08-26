'''
Faça um programa que pergunta a temperatura em graus Celsius e responde a temperatura correspondente em graus Fahrenheit.

Dica: se você digitar converta celsius para fahrenheit no Google, ele irá exibir a fórmula que você utilizará em seu programa e uma calculadora que pode auxiliar você na hora de testar seu programa.
'''

temp_C = float(input('Informe a temperatura em °C: '))

temp_F = temp_C * 9 / 5 + 32

print('A temperatura de {:.1f}°C corresponde a {:.1f}°F.'.format(temp_C, temp_F))
