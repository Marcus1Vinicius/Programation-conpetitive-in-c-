# Após um jantar em família, vocês decidem dividir igualmente o valor da conta, incluindo uma gorjeta de 10% sobre o valor total. Como o valor final nem sempre é perfeitamente divisível entre todos, é possível que algumas pessoas precisem pagar 1 centavo a mais para que a divisão feche corretamente. Escreva um programa que:

# Peça ao usuário o valor total da conta (sem gorjeta).
# Peça o número de pessoas que irão dividir a conta.
# Calcule o total da conta com a gorjeta de 10%, arredondando para o centavo mais próximo.
# Mostre:

# O valor total com gorjeta.
# O valor que cada pessoa deve pagar (parte inteira).
# Quantas pessoas precisam pagar 1 centavo a mais para completar exatamente o valor da conta.
# Valor total da conta: R$ 33.33
# Número de pessoas: 4

# Total com gorjeta: R$ 36.66
# Cada pessoa paga: R$ 9.16
# 2 pessoa(s) deve(m) pagar 1 centavo extra.

# Valor total da conta: R$ 100.5
# Número de pessoas: 3

# Total com gorjeta: R$ 110.55
# Cada pessoa paga: R$ 36.85
# 0 pessoa(s) deve(m) pagar 1 centavo extra.

conta = float(input("Digite o valor da compra: "))
qtd_pessoas = int(input("Digite quantas pessoas vão dividir a conta: "))
conta_gorjeta = round((conta * 0.10) + conta, 2)
conta_dividida = conta_gorjeta / qtd_pessoas
divisao_arredondada = round(conta_dividida, 2)

print(f"Total com gorjeta: {conta_gorjeta}\nCada pessoa paga: {divisao_arredondada}\n{int(divisao_arredondada % qtd_pessoas)} pessoa(s) deve(m) pagar 1 centavo extra")