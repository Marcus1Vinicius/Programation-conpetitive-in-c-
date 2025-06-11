# Um grupo de amigos foi a um restaurante e decidiu dividir a conta igualmente, mas um dos amigos não consumiu bebidas alcoólicas. Para que a divisão seja justa, o grupo resolveu que um único amigo que não consumiu bebidas alcoólicas não deve pagar essa parte da conta. Escreva um programa que receba como entrada o total da conta, o total apenas das bebidas alcóolicas e o número total de amigos que irão dividir a conta, incluindo o que não consumiu as bebidas. O programa deve calcular e exibir quanto o amigo que não bebeu pagará e quanto cada um dos outros amigos pagará. Considere que o número de amigos é sempre maior que 1.

# Total da conta: R$ 200
# Total apenas das bebidas: R$ 50
# Digite o número total de amigos: 4

# O amigo que não consumiu bebidas pagará: R$ 37.50
# Cada um dos outros amigos pagará: R$ 54.17

total_conta = float(input("Total da conta: R$ "))
total_bebidas = float(input("Total apenas das bebidas: R$ "))
total_amigos = int(input("Digite o número total de amigos: "))

amigo = (total_conta - total_bebidas) / total_amigos

amigos  = (total_conta - amigo) / (total_amigos - 1)

print(f"O amigo que não consumiu bebidas pagará: R$ {amigo}\nCada um dos outros amigos pagará: R$ {amigos}")

