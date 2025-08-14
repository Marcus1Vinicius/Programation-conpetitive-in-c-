# Você trabalha em uma clínica veterinária que cuida de diversos animais. A cada semana, é gerada uma lista com os nomes de todos os animais atendidos e outra lista com os respectivos pesos em quilogramas. A clínica está desenvolvendo um sistema que identifica quais animais precisam de atenção especial por estarem abaixo do peso mínimo saudável, definido como 5 kg. Escreva um programa que recebe para N animais definidos no início pelo usuário o nome e peso de cada animal. O programa deve exibir apenas os nomes dos animais cujo peso é inferior a 5 kg, no formato "nomeAnimal precisa de atenção!".

# Quantos animais foram atendidos? 3
# Nome do animal 1: Rex
# Peso do animal 1 (kg): 7.5
# Nome do animal 2: Mimi
# Peso do animal 2 (kg): 6.0
# Nome do animal 3: Toby
# Peso do animal 3 (kg): 4.3
# Toby precisa de atenção!

qtd_animais = int(input("Quantos animais foram atendidos? "))

lista_animais = []

for i in range(qtd_animais):
    nome = input(f"Nome do animal {i+1}: ")
    peso = float(input(f"Peso do animal {i+1} (kg): "))

    if peso < 5:
        lista_animais.append((nome, peso))

nomes = [animal[0] for animal in lista_animais]

for i in nomes:
    print(f"{i} precisa de atenção!")
