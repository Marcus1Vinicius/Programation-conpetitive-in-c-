# Em um esforço para otimizar os custos operacionais, a empresa de transporte urbano deseja calcular o consumo de combustível de seus ônibus em diferentes rotas. Cada ônibus registra a distância percorrida em quilômetros e a quantidade de combustível utilizada em litros. Escreva um programa que receba a distância total percorrida por um ônibus em uma rota e a quantidade de combustível consumida. O programa deve calcular e exibir a média de consumo de combustível em quilômetros por litro (km/l). Além disso, o programa deve indicar se o consumo está dentro do padrão de eficiência da empresa, que é considerado eficiente se o consumo for maior ou igual a 3 km/l.

# Digite a distância total percorrida (em km): 300
# Digite a quantidade de combustível consumida (em litros): 15
# Média de consumo: 20.00 km/l
# Consumo eficiente

distancia_total = float(input("Digite a distância total percorrida (em km): "))
consumo_combustivel = float(input("Digite a quantidade de combustível consumida (em litros): "))
media_consumo = distancia_total / consumo_combustivel

if(media_consumo >= 3):
    print("Média de consumo: ",media_consumo," km/l", "\nConsumo eficiente")

else:
    print("Média de consumo: ",media_consumo," km/l","\nConsumo ineficiente!")