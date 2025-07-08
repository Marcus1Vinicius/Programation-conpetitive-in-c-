# Desenvolva um programa que receba uma lista de consumo de energia (em kWh) de um edifício ao longo de 24 horas, com cada elemento representando o consumo de uma hora específica. O programa deve identificar e exibir as três horas consecutivas em que o consumo total foi o mais alto, no formato "Intervalo de maior consumo: X-Y horas", em que X é o valor de hora inicial e Y o valor de hora final do intervalo. Se houver mais de um período com o mesmo consumo total, exiba o primeiro encontrado.

consumo_energia = []

for i in range(24):

    energia = float(input(f"Digite o consumo da hora {i+1} em kWh: "))

    consumo_energia.append(energia)

maior_intervalo = 0

#     if consumo_energia == 3:
#         maior_intervalo1 = somar
 

# print("Intervalo de maior consumo: 18-20 horas")

# consumo_energia = []

# # Coletar os dados de consumo
# for i in range(24):
#     energia = float(input(f"Digite o consumo da hora {i} em kWh: "))
#     consumo_energia.append(energia)

# # Agora, vamos procurar o intervalo de 3 horas com maior consumo
# maior_soma = 0
# inicio_intervalo_maior = 0

# for i in range(0, 22):  # Vai até a hora 21, pois 21 + 2 = 23 (último índice possível)
#     soma_atual = sum(consumo_energia[i:i+3])  # Soma do intervalo de 3 horas
#     if soma_atual > maior_soma:
#         maior_soma = soma_atual
#         inicio_intervalo_maior = i

# # Exibir o resultado
# fim_intervalo_maior = inicio_intervalo_maior + 2
# print(f"\nIntervalo de maior consumo: {inicio_intervalo_maior}h às {fim_intervalo_maior}h")
# print(f"Consumo total nesse intervalo: {maior_soma:.2f} kWh")
