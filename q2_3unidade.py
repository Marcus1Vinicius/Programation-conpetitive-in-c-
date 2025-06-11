# Durante a parada em uma lanchonete na estrada, a família decidiu dividir as tarefas das compras para ganhar tempo. Os pais ficaram encarregados de escolher entre as saladas ou batatas fritas, enquanto as crianças escolheram quantos milkshakes gostariam de experimentar. Cada milkshake custa R$10. Desenvolva um programa que calcule a quantidade máxima de milkshakes que as crianças podem comprar, considerando o orçamento disponível, e quanto dinheiro sobraria após a compra. O programa deverá realizar as seguintes tarefas: Receber como entrada o valor do orçamento total das crianças. Calcular o número máximo de milkshakes que podem ser comprados sem exceder o orçamento e calcular a sobra do orçamento após a compra dos milkshakes.

# Digite o orçamento total das crianças: R$25.5
# Máximo de milkshakes que podem ser comprados: 2
# Sobra do orçamento: R$ 5.50

orcamento = float(input("Digite o orçamento total das crianças: R$"))

total_milk = int(orcamento / 10)

sobra = orcamento - (10 * total_milk)

print(f"Máximo de milkshakes que podem ser comprados: {total_milk}\nSobra do orçamento: R${sobra}")