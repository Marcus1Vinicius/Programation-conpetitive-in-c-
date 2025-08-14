# Em uma academia, o treinador faz o acompanhamento dos exercícios de sua aluna durante a semana. Ele precisa registrar a quantidade de repetições de um determinado exercício que a aluna realiza diariamente, para saber quantas repetições foram feitas ao todo durante a semana. Desenvolva um programa que peça ao treinador para inserir a quantidade de repetições de um exercício realizado pela aluna em cada um dos dias da semana. No final, o programa deve exibir o total de repetições realizadas ao longo da semana.

contador = 0
for i in range(7):
    repeticoes = int(input(f"Digite a quantidade de repetições feitas no dia {i+1}: "))
    contador += repeticoes
    
print(f"Total de repetições feitas na semana: {contador}")