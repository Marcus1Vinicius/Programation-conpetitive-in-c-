# Em uma competição organizada por um zoológico educativo, diversos animais participaram de uma corrida para descobrir qual deles é o mais rápido. Cada animal teve sua velocidade máxima registrada em km/h. Sua tarefa é criar um programa que ajude a identificar o animal mais rápido da corrida e também mostre a lista de todos os participantes. O programa deve continuar pedindo o nome e a velocidade máxima de cada animal até que o usuário digite 0 no campo do nome para indicar o fim da entrada. Ao final, o programa deve exibir a lista total de participantes (apenas com os nomes dos animais) e, também, o animal mais rápido junto com a sua velocidade máxima.

# Nome do animal (digite 0 para finalizar): Guepardo
# Velocidade máxima do Guepardo (km/h): 110
# Nome do animal (digite 0 para finalizar): Cavalo
# Velocidade máxima do Cavalo (km/h): 88
# Nome do animal (digite 0 para finalizar): Avestruz
# Velocidade máxima do Avestruz (km/h): 70
# Nome do animal (digite 0 para finalizar): 0

# Lista de participantes:
# Guepardo
# Cavalo
# Avestruz

# Animal mais rápido: Guepardo
# Velocidade: 110.0 km/h
animais = []
velocidades = []
lista_associada = []

while True:
    nome_animal = input("Nome do animal (digite 0 para finalizar): ")

    if nome_animal == "0":
        break

    velocidade_animal = float(input(f"Velocidade máxima do {nome_animal} (km/h): "))
    animais.append(nome_animal)
    velocidades.append(velocidade_animal)
    lista_associada.append((nome_animal, velocidade_animal))

print("\nLista de participantes:")
for animal in animais:
    print(f"{animal}")

if lista_associada:
    animal_mais_rapido = max(lista_associada, key=lambda x: x[1])
    print(f"\nAnimal mais rápido: {animal_mais_rapido[0]}")
    print(f"Velocidade: {animal_mais_rapido[1]} km/h")
else:
    print("\nNenhum animal foi cadastrado")
    