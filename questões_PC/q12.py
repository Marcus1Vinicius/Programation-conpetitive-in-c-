# Em uma escola urbana inovadora, os alunos são agrupados em turmas rotativas a cada trimestre para encorajar a interação com diferentes colegas e professores, e participar de desafios de equipe. Escreva um programa que receba a nota de um aluno e determine o comentário apropriado sobre seu desempenho no desafio de colaboração do trimestre. Se a nota for inferior a 50, o comentário deve ser 'ruim, precisa melhorar'; se estiver entre 50 e 74, o comentário deve ser 'bom, mas pode melhorar'; e se for 75 ou mais, o comentário deve ser 'Excelente'. O programa deve solicitar ao usuário o nome e a nota do aluno e exibir a mensagem no formato: '[Nome] teve um desempenho [comentário]' no desafio de colaboração.

# Digite o nome do aluno: Carlos
# Digite a nota do aluno: 49
# Carlos teve um desempenho ruim, precisa melhorar no desafio de colaboração

nome_aluno = input("Digite o nome do aluno: ")
nota_aluno = int(input("Digite a nota do aluno: "))

if(nota_aluno >= 75):
    print(nome_aluno," teve um desempenho Excelente")

elif(nota_aluno < 50):
    print(nome_aluno," teve um desempenho ruim, precisa melhorar no desafio de colaboração")

else:
    print(nome_aluno," teve um desempenho bom, mas pode melhorar")