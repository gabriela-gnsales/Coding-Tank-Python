'''
Faça um programa que pergunta a temperatura em graus Fahrenheit e responde a temperatura correspondente em graus Celsius.

Atenção: apenas trocar "celsius" e "fahrenheit" na equação utilizada no exercício anterior não é a solução. Você deve realizar a inversão completa da fórmula (ou utilizar o mesmo truque para consultar essa fórmula no Google).
'''

temp_F = float(input('Informe a temperatura em °F: '))

temp_C = (temp_F - 32) * 5 / 9

print('A temperatura de {:.1f}°F corresponde a {:.1f}°C.'.format(temp_F, temp_C))
