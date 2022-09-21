
tensao = float(input('Informe o valor da tensão da bateria: '))
resistor1 = float(input('Informe o valor do resistor em paralelo R1: '))
resistor2 = float(input('Informe o valor do resistor em paralelo R2: '))

resistencia_equivalente = (resistor1 * resistor2) / (resistor1 + resistor2)
corrente_eletrica = tensao / resistencia_equivalente

print(f'A resistência equivalente do circuito é {resistencia_equivalente:.2f} e o valor da corrente que fluirá por ele é {corrente_eletrica:.2f}.')
