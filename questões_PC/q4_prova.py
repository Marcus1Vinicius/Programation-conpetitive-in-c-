# Uma empresa de aluguel de bicicletas deseja saber quantas bicicletas foram alugadas em cada dia da semana com base em uma lista de informações de aluguel. Você deverá criar um programa que recebe o total de bicicletas alugadas durante uma semana, de segunda-feira a domingo, como uma lista de números inteiros. O programa deve solicitar ao usuário que insira o número de bicicletas alugadas a cada dia, começando da segunda-feira até o domingo. Então, o programa deve exibir qual foi o dia da semana com o maior número de aluguéis. 

# Entrada:

# - 7 inteiros representando a quantidade de bicicletas alugadas de segunda-feira a domingo, um por linha

# Saída:

# - Uma string no formato 'O dia com mais alugueis foi {dia}.' onde {dia} é o dia da semana correspondente. Caso o mesmo número máximo de bicicletas seja alugado em mais de um dia, o programa deve retornar o primeiro dia que atingiu esse valor.

# Dicas:

# - Use a seguinte lista para armazenar os nomes dos dias da semana: ['segunda-feira', 'terça-feira', 'quarta-feira', 
#'quinta-feira', 'sexta-feira', 'sábado', 'domingo']

dias_semana = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
lista_qtd_por_dia = []

for dia in dias_semana:
    qtd = int(input(f"Digite quantas bicicletas foram alugadas na {dia}: "))
    lista_qtd_por_dia.append(qtd)

max_alugueis = max(lista_qtd_por_dia)
indice_dia = lista_qtd_por_dia.index(max_alugueis)
dia_mais_alugueis = dias_semana[indice_dia]

print(f'O dia com mais alugueis foi {dia_mais_alugueis}.')
