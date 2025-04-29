# Durante o acompanhamento do paciente com dor no joelho, o fisioterapeuta decidiu desenvolver um plano de tratamento específico. Este plano inclui uma fórmula para calcular a intensidade semanal das sessões de fisioterapia necessárias em função do nível de dor relatado pelo paciente e do número de semanas de tratamento já concluídas. A intensidade I (em horas) é dada pela função linear I(n) = 2 * n + 3 * dor, onde n é o número de semanas já realizadas e dor é o escore de dor do paciente em uma escala de 1 a 10. Escreva um programa que receba o número de semanas concluídas e o escore de dor do paciente e retorne a intensidade semanal das sessões de fisioterapia.

# Digite o número de semanas concluídas: 5
# Digite o escore de dor do paciente (1 a 10): 5
# Intensidade semanal das sessões de fisioterapia: 25 horas

n = int(input("Digite o número de semanas concluídas: "))
dor = int(input("Digite o escore de dor do paciente (1 a 10): "))
formula = 2 * n + 3 * dor
print("Intensidade semanal das sessões de fisioterapia:", formula,"horas")