# No departamento de Recursos Humanos, é necessário otimizar o escalamento de treinamentos para os funcionários, garantindo que cada funcionário participe de um determinado número de horas de treinamento por mês. Escreva um programa que receba como entrada a quantidade total de horas de treinamento disponível em um mês, o número de funcionários e a carga horária mínima que cada funcionário deve cumprir. O programa deve calcular e retornar o número máximo de funcionários que podem ser escalados para treinamento naquele mês, garantindo que cada um cumpra a carga horária mínima estipulada.

# Digite a quantidade total de horas de treinamento disponível no mês: 100
# Digite o número de funcionários: 14
# Digite a carga horária mínima que cada funcionário deve cumprir: 16
# Número máximo de funcionários que podem ser escalados: 6

horas_treinamento = int(input("Digite a quantidade total de horas de treinamento disponível no mês: "))
qtd_funcionarios = int(input("Digite o número de funcionários: "))
carga_hor_minima = int(input("Digite a carga horária mínima que cada funcionário deve cumprir: "))

formula = int(horas_treinamento / carga_hor_minima)

print("Número máximo de funcionários que podem ser escalados: ", formula)

# 16 * x = 100
# 