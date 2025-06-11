# Em uma escola, cada turma possui uma lista de estudantes e suas respectivas notas finais. Sua tarefa é calcular a média da nota de todos os estudantes de cada turma e identificar qual turma teve a melhor média.

# Considere que você receberá as notas de cada turma diretamente, e seu programa deve calcular a média de notas de cada uma. 

# Entrada:

# 1. Um número inteiro 't', representando o número de turmas.

# 2. Para cada turma, uma primeira linha contendo um número inteiro 'n', que representa o número de estudantes na turma.

# 3. As próximas 'n' linhas para cada turma contêm a nota do estudante (número inteiro).

# Saída:

# - Calcule e imprima a média das notas de cada turma.

# - Imprima o índice (baseado em zero) da turma com a melhor média, no formato: “Melhor turma: índice”.

# Entre com o número de turmas: 2
# Indique o número de estudantes da turma 1:3
# Entre com a nota do aluno 1: 50
# Entre com a nota do aluno 2: 78
# Entre com a nota do aluno 3: 91
# Média da turma 1: 73.00
# Indique o número de estudantes da turma 2:2
# Entre com a nota do aluno 1: 40
# Entre com a nota do aluno 2: 60
# Média da turma 2: 50.00
# Melhor turma: 1

qtd_turmas = int(input("Entre com o número de turmas: "))
medias_turmas = []

for turma in range(qtd_turmas):
    qtd_estudantes = int(input(f"Indique o número de estudantes da turma {turma+1}: "))
    notas_turma = []
    
    for estudante in range(qtd_estudantes):
        nota = float(input(f"Entre com a nota do aluno {estudante+1}: "))
        notas_turma.append(nota)
    
    media = sum(notas_turma) / len(notas_turma)
    medias_turmas.append(media)
    print(f"Média da turma {turma+1}: {media:.2f}")

indice_melhor = medias_turmas.index(max(medias_turmas))

print(f"Melhor turma: {indice_melhor+1}")