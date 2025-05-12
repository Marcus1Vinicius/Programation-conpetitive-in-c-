# Com o avanço dos serviços bancários digitais, muitos bancos passaram a adotar sistemas de senhas eletrônicas para melhorar o atendimento. Isso, porém, representa um desafio para clientes que não estão familiarizados com tecnologia, como alguns idosos. Imagine que um banco possui um sistema de senhas eletrônicas geradas para atendimento em caixas automáticos. Este banco tem uma lista de senhas já emitidas para o dia composta por: 'A125', 'B234', 'C341', 'A456', 'B567', 'C678', 'A789'. Crie um programa que exibe a lista de senhas emitidas e solicita ao usuário que insira uma senha. O programa deve verificar se a senha inserida pelo usuário existe na lista de senhas emitidas. Se a senha estiver presente, o sistema deverá exibir a mensagem 'Senha reconhecida, prossiga com o atendimento!'; caso contrário, a mensagem deverá ser 'Senha não reconhecida, por favor, dirija-se ao atendimento.'.

# Lista de senhas emitidas:
# A125
# B234
# C341
# A456
# B567
# C678
# A789
# Por favor, insira sua senha: A125
# Senha reconhecida, prossiga com o atendimento!

senhas_emitidas = ["A125", "B234", "C341", "A456", "B567", "C678", "A789"]

print(f"Lista de senhas emitidas: \n {senhas_emitidas}")

sua_senha = input("Por favor, insira sua senha: ")

if sua_senha in senhas_emitidas:
    print("Senha reconhecida, prossiga com o atendimento!")

else:
    print("Senha não reconhecida, por favor, dirija-se ao atendimento.")