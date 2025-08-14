# Você está desenvolvendo um sistema para registrar participantes de um evento. O sistema deve permitir que o organizador registre os nomes dos participantes, mas não pode permitir que o mesmo nome seja registrado mais de uma vez. Primeiro, o programa deve solicitar ao organizador o número de participantes que ele deseja registrar. Em seguida, permitir que o organizador insira o nome de cada participante. O sistema deve verificar se o nome já foi registrado anteriormente. Caso o nome já tenha sido informado, o programa deve informar ao organizador que aquele nome já foi registrado ('Nome já cadastrado!') e pedir para ele inserir outro nome. O sistema deve continuar pedindo o nome dos participantes até que o número total de participantes seja atingido. Ao final, o programa deve exibir a lista de todos os participantes registrados.

# Digite o número de participantes: 3
# Digite o nome do participante 1: João
# Digite o nome do participante 2: Maria
# Digite o nome do participante 3: João
# Nome já cadastrado!
# Digite o nome do participante 3: Pedro

# Participantes registrados:
# 1. João
# 2. Maria
# 3. Pedro

qtd_participantes = int(input("Digite o número de participantes: "))
lista_participantes = []

for i in range(qtd_participantes):      
    while True: 
        nome = input(f"Digite o nome do participante {i+1}: ")
        if nome in lista_participantes:
                print("Nome já cadastrado!")
        else:
            lista_participantes.append(nome)
            break

print(f"Participantes registrados:")
for i, nome in enumerate(lista_participantes):
    print(f"{i+1}. {nome}")