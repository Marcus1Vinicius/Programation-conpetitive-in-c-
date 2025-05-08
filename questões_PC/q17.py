# João, após uma corrida matinal, decidiu experimentar um novo sanduíche especial recomendado na lanchonete. Inspirado por sua escolha, ele quer criar um pequeno sistema para acompanhar quantos sanduíches especiais ele pode comer no mês sem ultrapassar seu orçamento mensal. Para isso, desenvolva um programa que peça ao usuário entrada para o preço de cada sanduíche especial consumido, um por um. O sistema deve continuar a registrar as entradas até que o usuário digite -1, indicando que não deseja registrar mais sanduíches. Ao final, o programa deve exibir o número total de sanduíches especiais consumidos e somar o valor total gasto nesses sanduíches. Se não houver registros (caso o usuário insira -1 de imediato), deve-se exibir que nenhum sanduíche foi consumido e o total gasto deve ser zero.

# Digite o preço do sanduíche especial ou -1 para encerrar: 5.0
# Digite o preço do sanduíche especial ou -1 para encerrar: 10.0
# Digite o preço do sanduíche especial ou -1 para encerrar: -1
# Total de sanduíches consumidos: 2
# Total gasto: 15.0

contador = 0 
contador1 = 0

while True:
    sanduiches = float(input("Digite o preço do sanduíche especial ou -1 para encerrar: "))

    if sanduiches == -1:
        break

    elif sanduiches > 0:
        contador += sanduiches
        contador1 += 1

print("Total de sanduíches consumidos: ", contador1, '\nTotal gasto: ', contador)
