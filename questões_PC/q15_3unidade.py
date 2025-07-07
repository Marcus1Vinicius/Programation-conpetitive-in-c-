# João, após uma corrida matinal, decidiu experimentar um novo sanduíche especial recomendado na lanchonete. Inspirado por sua escolha, ele quer criar um pequeno sistema para acompanhar quantos sanduíches especiais ele pode comer no mês sem ultrapassar seu orçamento mensal. Para isso, desenvolva um programa que peça ao usuário entrada para o preço de cada sanduíche especial consumido, um por um. O sistema deve continuar a registrar as entradas até que o usuário digite -1, indicando que não deseja registrar mais sanduíches. Ao final, o programa deve exibir o número total de sanduíches especiais consumidos e somar o valor total gasto nesses sanduíches. Se não houver registros (caso o usuário insira -1 de imediato), deve-se exibir que "Nenhum sanduíche foi consumido." e o total gasto deve ser zero.

contador = 0 
contador1 = 0

while True:
    sanduiches = float(input("Digite o preço do sanduíche especial ou -1 para encerrar: "))

    if sanduiches == -1:
        break

    elif sanduiches > 0:
        contador += sanduiches
        contador1 += 1

if sanduiches > 0:
    print("Total de sanduíches consumidos: ", contador1, '\nTotal gasto: ', contador)
    
else:
    print("Nenhum sanduíche foi consumido", '\nTotal gasto: ', contador)







