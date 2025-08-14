# A biblioteca comunitária deseja implementar um sistema simples para monitorar a quantidade de empréstimos realizados por cada usuário em um determinado mês. O sistema deve ser capaz de receber, para cada usuário, o nome e a quantidade de empréstimos realizados. O programa deve solicitar ao usuário que insira o nome e a quantidade de empréstimos para cada usuário, repetindo o processo até que uma entrada vazia seja fornecida para o nome do usuário. O objetivo final é exibir uma lista com o nome de cada usuário seguido pela quantidade de empréstimos que ele realizou, no formato "nome: N empréstimos.". Assuma que não há limite para a quantidade de empréstimos que um usuário pode realizar.

# Digite o nome do usuário (ou pressione Enter para finalizar): Vinicius
# Digite a quantidade de empréstimos realizados por Vinicius: 40
# Digite o nome do usuário (ou pressione Enter para finalizar): Pedro
# Digite a quantidade de empréstimos realizados por Pedro: 20
# Digite o nome do usuário (ou pressione Enter para finalizar): Diego
# Digite a quantidade de empréstimos realizados por Diego: 10
# Digite o nome do usuário (ou pressione Enter para finalizar):

# Lista de usuários e seus empréstimos:
# Vinicius: 40 empréstimos
# Pedro: 20 empréstimos
# Diego: 10 empréstimos

usuarios = []
emprestimos = []
associados = []

while True:

    nome = input("Digite o nome do usuário (ou pressione Enter para finalizar): ")

    if nome == "":
        break

    usuarios.append(nome)

    qtd_emprestimo = int(input(f"Digite a quantidade de empréstimos realizados por {nome}: "))
    emprestimos.append(qtd_emprestimo)

    associados.append((nome, qtd_emprestimo))

for usuarios, emprestimos in associados:
    print(f"{usuarios}: {emprestimos} empréstimos")


# print(f"Lista de usuários e seus empréstimos:\n{associados}: empréstimos")



        