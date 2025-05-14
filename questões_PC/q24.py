# Você foi designado para criar um programa que auxilie um professor a organizar as notas de seus alunos em uma turma. O professor deseja saber a média das notas e identificar quais alunos tiraram uma nota acima da média. As notas são inteiras, variando de 0 a 10.

# O programa deve começar solicitando ao usuário o número de alunos na turma (n), que será inserido por meio de um input. Em seguida, o programa deve coletar as notas dos alunos, armazenando-as em uma lista. Após registrar todas as notas, o programa calculará a média de todas as notas da turma e, por fim, imprimirá a média e a lista de notas que estão acima da média.

# Quantos alunos há na turma? 3
# Digite a nota do aluno 1: 5
# Digite a nota do aluno 2: 8
# Digite a nota do aluno 3: 10

# Média das notas: 7.67
# Notas acima da média: 8 10

qtd_alunos = int(input("Quantos alunos há na turma? "))
notas = []
media = 0
notas_acima = []

for i in range(qtd_alunos):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    media = media + nota
    notas.append(nota)

media = media / qtd_alunos

for i in notas:
    if i > media:
        notas_acima.append(i)

print(f"Média das notas: {media}\nNotas acima da média: {notas_acima}")
    