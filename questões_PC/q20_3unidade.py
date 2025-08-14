# Desenvolva um programa que receba uma lista de consumo de energia (em kWh) de um edifício ao longo de 24 horas, com cada elemento representando o consumo de uma hora específica. O programa deve identificar e exibir as três horas consecutivas em que o consumo total foi o mais alto, no formato "Intervalo de maior consumo: X-Y horas", em que X é o valor de hora inicial e Y o valor de hora final do intervalo. Se houver mais de um período com o mesmo consumo total, exiba o primeiro encontrado.


consumo_energia = []

for i in range(1, 25):
    energia = float(input(f"Digite o consumo da hora {i} em kWh: "))
    consumo_energia.append(energia)

maior_soma = 0
inicio_maior_intervalo = 0

for i in range(22): 
    soma_atual = consumo_energia[i] + consumo_energia[i+1] + consumo_energia[i+2]

    if soma_atual > maior_soma:
        maior_soma = soma_atual
        inicio_maior_intervalo = i

print(f"Intervalo de maior consumo: {inicio_maior_intervalo + 1}-{inicio_maior_intervalo + 3} horas")