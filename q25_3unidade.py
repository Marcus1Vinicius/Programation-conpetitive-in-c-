# Em um edifício comercial, é essencial prever o consumo de energia durante os horários de pico para evitar sobrecargas e otimizar o uso de energia. Considere que o edifício possui diversos equipamentos eletrônicos, cada um com um consumo energético específico por hora de operação.
# Escreva um programa que pergunte ao usuário quantos equipamentos serão inseridos. Em seguida, para cada equipamento, solicite o nome, o consumo energético por hora (em kWh) e o número de horas que ele opera durante o horário de pico. Depois, o programa também deve solicitar o limite máximo de consumo energético permitido para o horário de pico. O programa deve calcular o consumo total e, ao final, deve informar o consumo total e indicar se esse valor excede o limite estabelecido.
# Implemente uma função chamada calcular_consumo_total(equipamentos, limite) que receba como parâmetros a lista de equipamentos e o limite de consumo. A função deve retornar o consumo total e uma mensagem informando se o consumo está dentro do limite ("O consumo total está dentro do limite.") ou se o excede ("O consumo total excede o limite.").

# Quantos equipamentos deseja inserir? 3

# Equipamento 1:
# Nome do equipamento: Geladeira
# Consumo por hora (kWh): 0.12
# Horas de uso por dia: 24

# Equipamento 2:
# Nome do equipamento: Tv
# Consumo por hora (kWh): 0.3
# Horas de uso por dia: 12

# Equipamento 3:
# Nome do equipamento: Fogão elétrico
# Consumo por hora (kWh): 3
# Horas de uso por dia: 4

# Limite de consumo diário (kWh): 20

# Consumo total: 18.48 kWh
# O consumo total está dentro do limite.

def calcular_consumo_total(equipamentos, limite):
    consumo_total = 0

    for equipamento in equipamentos:
        nome, consumo_hora, horas_uso = equipamento
        consumo_total += consumo_hora * horas_uso

    if consumo_total <= limite:
        mensagem = "O consumo total está dentro do limite."
    else:
        mensagem = "O consumo total excede o limite."

    return consumo_total, mensagem

equipamentos = []
qtd = int(input("Quantos equipamentos deseja inserir? "))

for i in range(qtd):
    print(f"\nEquipamento {i+1}:")
    nome = input("Nome do equipamento: ")
    consumo = float(input("Consumo por hora (kWh): "))
    horas = int(input("Horas de uso por dia: "))

    equipamentos.append((nome, consumo, horas))

limite = float(input("\nLimite de consumo diário (kWh): "))

total, status = calcular_consumo_total(equipamentos, limite)

print(f"\nConsumo total: {total:.2f} kWh")
print(status)

