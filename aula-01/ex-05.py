# Faça um programa que pergunte para a motorista a distância que ela dirigiu e o tempo que seu trajeto levou, e responda sua velocidade média.

distancia = float(input('Qual a distância, em km, que você dirigiu? '))
tempo = float(input('Quanto tempo, em minutos, você levou em seu trajeto? '))

velocidade = distancia / (tempo / 60)

print(f'Sua velocidade média foi de {velocidade:.1f} km/h.')
