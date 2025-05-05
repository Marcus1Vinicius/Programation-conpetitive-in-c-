# Em um evento de casamento, cada convidado deve receber uma lembrancinha ao final da festa. No entanto, devido a restrições de orçamento e disponibilidade de materiais, a quantidade de lembrancinhas é limitada. Escreva um programa que receba o número total de convidados confirmados e o número total de lembrancinhas disponíveis. O programa deve calcular e exibir quantas lembrancinhas cada convidado receberá de modo que todos recebam a mesma quantidade possível, e exibir quantas lembrancinhas, se houver, sobrarão. Caso o número de convidados seja maior que a quantidade de lembrancinhas, informe que não há lembrancinhas suficientes para todos os convidados.

# Digite o número total de convidados confirmados: 10
# Digite o número total de lembrancinhas disponíveis: 5
# Não há lembrancinhas suficientes para todos os convidados.

qtd_convidados = int(input("Digite o número total de convidados confirmados: "))
total_lembrancinha = int(input("Digite o número total de lembrancinhas disponíveis: "))
c = int(total_lembrancinha / qtd_convidados)
if(c >= 1):
    print("Cada convidado receberá: ",c,"lembrancinhas\nLembrancinhas sobrando: ", total_lembrancinha % qtd_convidados)
else:
    print("Não há lembrancinhas suficientes para todos os convidados.")