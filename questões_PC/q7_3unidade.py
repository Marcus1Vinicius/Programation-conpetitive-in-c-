# Em uma escola internacional que utiliza um sistema de aprendizagem baseado em competência, as turmas são formadas por alunos de diferentes idades, agrupados conforme suas habilidades em cada matéria. Neste cenário, a escola decidiu introduzir critérios para progressão dos alunos em matemática, levando em conta seu desempenho em dois testes específicos - Teste A e Teste B. O aluno deve progredir para o próximo nível em matemática se, e somente se: a média dos dois testes for maior ou igual a 70; caso a média esteja entre 50 e 69, o aluno deve realizar um teste adicional de recuperação, cujo resultado deve ser igual ou superior a 65 para que o aluno possa progredir. Se a nota média for inferior a 50, o aluno deve repetir o nível. Implemente um programa que receba as notas dos Testes A e B, e do teste de recuperação, e imprima se o aluno 'Progride', 'Progride após Recuperação', ou 'Repete'. O programa deve solicitar ao usuário as notas dos Testes A e B como números inteiros ou decimais, e, se necessário, a nota do teste de recuperação.

t1 = float(input("Nota do teste A: "))
t2 = float(input("Nota do teste B: "))
m = (t1 + t2) / 2

if m > 69:
    print("Progride")

elif m > 49:
    t3 = float(input("Digite a nota do teste de recuperação: "))
    m1 = (t1+t2+t3) / 3
    if m1 > 50:
        print("Progride após Recuperação")
    else:
        print("Repete")

else:
    print("Repete")