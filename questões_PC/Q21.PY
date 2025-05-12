# A biblioteca pública deseja implementar um sistema simples para verificar a disponibilidade de livros antes de realizar empréstimos. Você deve escrever um programa que receba o número de livros já emprestados, os seus títulos separadamente, e, depois, um título específico de livro que um membro deseja emprestar. O programa deve verificar se o título do livro desejado está disponível para empréstimo. Se o livro estiver disponível (ou seja, não estiver na lista de livros emprestados), o programa deve exibir uma mensagem informando que o livro pode ser emprestado. Caso contrário, deve exibir uma mensagem informando que o livro já está emprestado e não está disponível no momento.



# Digite o número de livros atualmente emprestados: 0
# Digite o título do livro que deseja emprestar: O Alquimista
# O livro pode ser emprestado.

qtd_livros_emprestados = int(input("Digite o número de livros atualmente emprestados: "))
livros = []

for i in range(qtd_livros_emprestados):
    qual_livro = input(f"Digite o título do livro emprestado {i+1}: ")
    livros.append(qual_livro)

emprestimo = input("Digite o título do livro que deseja emprestar: ")

if emprestimo in livros:
    print("O livro já está emprestado e não está disponível no momento.")

else:
    print("O livro pode ser emprestado.")