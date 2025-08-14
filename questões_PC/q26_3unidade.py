# A academia deseja implementar um sistema de recompensas para incentivar os membros a frequentarem mais aulas. Cada membro pode acumular pontos com base na frequência das aulas semanais. O sistema de recompensas funciona da seguinte forma:

# - Cada aula frequentada concede 10 pontos ao membro.
# - Se o membro frequentar 5 ou mais aulas em uma semana, ele recebe um bônus de 50 pontos adicionais.
# - No final de cada mês, os pontos são acumulados e convertidos em recompensas.

# Escreva um programa que calcule o total de pontos acumulados por um membro em uma semana com base no número de aulas frequentadas. O programa deve definir uma função que receba como entrada o número de aulas frequentadas na semana e retorne o total de pontos ganhos.

# Digite o número de aulas frequentadas na semana: 4
# Total de pontos acumulados na semana: 40

def recompensa(frequencia):
    pontos = 10 * frequencia

    if frequencia > 4:
        pontos += 50

    return pontos


qtd_aulas = int(input("Digite o número de aulas frequentadas na semana: "))
formula = recompensa(qtd_aulas)


print(f"Total de pontos acumulados na semana: {formula}")

