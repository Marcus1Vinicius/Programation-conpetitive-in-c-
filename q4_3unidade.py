# Com a introdução de turmas híbridas, as escolas têm agora desafios adicionais na gestão de horários e recursos. Um dos desafios é a alocação de tempo entre aulas presenciais e online para garantir que cada turma siga o currículo de forma equilibrada. Suponha que você precise desenvolver um programa simples que ajude na divisão do tempo disponível em um dia de aula entre as duas modalidades. O programa deve primeiro solicitar ao usuário para digitar o total de horas de aula no dia (um número inteiro). Em seguida, o programa deve solicitar o percentual de tempo que será destinado às aulas presenciais (um número inteiro entre 0 e 100). Com base nisso, o programa deve calcular quantas horas serão dedicadas às aulas presenciais e quantas horas às aulas online. O cálculo deve considerar apenas inteiros, utilizando operadores matemáticos para arredondar conforme necessário e garantir que a soma das horas seja igual ao total.

# Digite o total de horas de aula no dia: 8
# Digite o percentual de tempo para aulas presenciais (0 a 100): 50
# Horas para aulas presenciais: 4
# Horas para aulas online: 4

total_horas_aula = int(input("Digite o total de horas de aula no dia: "))

percentual_tempo = int(input("Digite o percentual de tempo para aulas presenciais (0 a 100): "))

hora_presencial = total_horas_aula * (percentual_tempo / 100)

hora_online = total_horas_aula - hora_presencial

print(f"Horas para aulas presenciais: {hora_presencial}\nHoras para aulas online: {hora_online}")