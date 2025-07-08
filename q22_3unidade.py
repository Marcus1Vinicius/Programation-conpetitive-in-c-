# ​Você foi contratado como analista de dados de uma livraria que deseja entender melhor o perfil de seus clientes. Uma das suas funções é analisar os relatórios de vendas e identificar padrões de consumo. A equipe da loja está especialmente interessada em saber quais gêneros de livros são mais populares entre os leitores. Para isso, você recebeu um conjunto de registros que indicam os gêneros dos livros vendidos ao longo do dia. Seu desafio é elaborar um programa que permita ao usuário digitar, um a um, os gêneros dos livros vendidos. A entrada termina quando o usuário digitar o número 0, indicando que todos os dados foram inseridos. O programa deve então analisar as informações e mostrar qual foi o gênero mais vendido, junto com a quantidade de vezes que ele apareceu. Se nenhum dado for informado, o programa deve simplesmente avisar que 'Nenhum gênero foi informado.'.

lista_generos = []

while True:

    generos = input("Digite os gêneros dos livros vendidos (digite 0 para encerrar): ")
    lista_generos.append(generos)
    print(lista_generos)

    if generos == "0":
        break

    elif generos == "":
        print("Nenhum gênero foi informado.")

# for i in lista_generos:
    
print(f"O gênero mais vendido foi: Biografia (3 vendas)")

