# Em uma escola localizada em uma pequena cidade, os alunos têm a oportunidade de escolher entre turmas organizadas por projetos temáticos, como sustentabilidade, tecnologia ou artes. Ao longo do ano, eles trabalham em projetos específicos, usando princípios interdisciplinares que envolvem matemática, ciência e línguas. A escola deseja automatizar o processo de alocação de alunos nas turmas, baseado no seu interesse principal. O objetivo é criar um pequeno programa que receba o nome do aluno e sua escolha de temática. Se o aluno escolher 'sustentabilidade', o sistema deve alocá-lo na turma de sustentabilidade. Se o aluno escolher 'tecnologia' ou 'artes', o sistema deve alocá-lo na turma correspondente. Para qualquer outra escolha, alocá-lo na turma de escolha geral, indicando que a temática escolhida não faz parte das opções principais oferecidas. Desenvolva um programa que faz essa alocação para um aluno e imprime uma mensagem indicando a que turma ele pertence.

# Digite o nome do aluno: João
# Digite a escolha de temática (sustentabilidade, tecnologia, artes): sustentabilidade
# O aluno João foi alocado na turma de sustentabilidade.

nome_aluno = input("Digite o nome do aluno: ")
escolha_tematica = input("Digite a escolha de temática (sustentabilidade, tecnologia, artes): ")

if(escolha_tematica == "sustentabilidade" or escolha_tematica == "tecnologia" or escolha_tematica == "artes"):
    print("O aluno", nome_aluno ," foi alocado na turma de ",escolha_tematica)
else:
    print("O aluno", nome_aluno ," foi alocado na turma de escolha geral.")