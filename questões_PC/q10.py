# Desenvolva um programa para ajudar os gerentes de projeto a alocar tarefas aos membros da equipe com base em sua disponibilidade semanal. Cada membro da equipe tem um número máximo de horas que pode trabalhar por semana. O programa deve receber três entradas: a quantidade de horas já alocadas a um membro da equipe (número inteiro), o número de horas necessárias para uma nova tarefa (número inteiro) e o limite semanal de horas do membro (número inteiro). Se a soma das horas já alocadas e as horas da nova tarefa não ultrapassar o limite semanal de horas do membro, o programa deve exibir uma mensagem informando que o membro pode receber a nova tarefa. Caso contrário, deve exibir uma mensagem indicando que o membro não está disponível para a nova tarefa.

# Digite a quantidade de horas já alocadas ao membro: 0
# Digite o número de horas necessárias para a nova tarefa: 10
# Digite o limite semanal de horas do membro: 15
# O membro pode receber a nova tarefa.

qtd_horas_alocados = int(input("Digite a quantidade de horas já alocadas ao membro: "))
horas_necessaria_tarefa = int(input("Digite o número de horas necessárias para a nova tarefa: "))
limite_semanal_horas = int(input("Digite o limite semanal de horas do membro: "))