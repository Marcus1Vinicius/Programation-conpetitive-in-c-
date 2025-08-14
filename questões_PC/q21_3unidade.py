# O restaurante precisa garantir que todos os ingredientes necessários para preparar os pratos do menu estejam sempre disponíveis. No entanto, alguns ingredientes podem estar próximos de acabar, e é crucial identificar esses casos para que o restaurante possa providenciar a reposição a tempo. Escreva um programa que receba uma lista de ingredientes e suas respectivas quantidades em estoque. O programa deve exibir uma lista de ingredientes que estão abaixo de uma quantidade mínima estabelecida, no formato "nomeIngrediente - X unidades". Considere que a quantidade mínima para todos os ingredientes é de 5 unidades. O usuário deve informar a quantidade de ingredientes e, em seguida, para cada ingrediente, informar o nome e a quantidade em estoque.

# Digite a quantidade de ingredientes: 3
# Digite o nome do ingrediente 1: Galinha
# Digite a quantidade em estoque de Galinha: 10
# Digite o nome do ingrediente 2: Batata
# Digite a quantidade em estoque de Batata: 4
# Digite o nome do ingrediente 3: Manteiga
# Digite a quantidade em estoque de Manteiga: 6
# Ingredientes abaixo da quantidade mínima:
# Batata - 4 unidades

qtd_ingredientes = int(input("Digite a quantidade de ingredientes: "))

lista_ingredientes = []

lista_qtd_estoque_ingredientes = []

associados = []

for i in range(qtd_ingredientes):

    nome_ingrediente = input(f"Digite o nome do ingrediente {i+1}: ")
    lista_ingredientes.append(nome_ingrediente)

    qtd_estoque_ingrediente = int(input(f"Digite a quantidade em estoque de {nome_ingrediente}: "))
    lista_qtd_estoque_ingredientes.append(qtd_estoque_ingrediente)

    if qtd_estoque_ingrediente < 5:  
        associados.append((nome_ingrediente, qtd_estoque_ingrediente))

for lista_ingredientes, lista_qtd_estoque_ingredientes in associados:
    
        print(f"Ingredientes abaixo da quantidade mínima:\n{lista_ingredientes} - {lista_qtd_estoque_ingredientes} unidades")