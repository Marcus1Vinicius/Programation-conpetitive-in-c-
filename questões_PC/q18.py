# Com a introdução de frotas de caminhões elétricos ou movidos a combustíveis alternativos, é importante para uma transportadora monitorar a autonomia dos caminhões em diferentes condições de carga e trajeto. Implemente um programa que receba a autonomia inicial de um caminhão (em quilômetros) como um número inteiro e o número de viagens que ele realizará, também como um número inteiro. Para cada viagem, o usuário deve informar a distância percorrida como um número inteiro. Se a autonomia atingir 100 km ou menos após uma viagem, exiba uma mensagem para indicar que é hora de carregar o caminhão e continue para a próxima viagem.Finalize o recebimento de dados quando a autonomia acabar (ou seja, atingir 0 km ou menos). No final, exiba a autonomia restante após todas as viagens ou até que a autonomia tenha acabado.

# Digite a autonomia inicial do caminhão (em km): 200
# Digite o número de viagens: 3
# Digite a distância percorrida na viagem 1 (em km): 50
# Digite a distância percorrida na viagem 2 (em km): 60
# Hora de carregar o caminhão!
# Digite a distância percorrida na viagem 3 (em km): 90
# Autonomia restante: 0 km

autonomia = int(input("Digite a autonomia inicial do caminhão (em km): "))
qtd_viagens = int(input("Digite o número de viagens: "))
contador = 0
for i in range(qtd_viagens):
    distancia_percorrida = int(input(f"Digite a distância percorrida na viagem {i+1} (em km): "))
    contador = contador + distancia_percorrida
    autonomia = autonomia - distancia_percorrida
    if(autonomia < 100):
        print("Hora de carregar o caminhão!")
    
print("Autonomia restante: ", autonomia, "km")