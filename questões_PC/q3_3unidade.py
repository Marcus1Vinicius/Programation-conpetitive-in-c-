# No contexto das cidades inteligentes, um dos desafios é otimizar o fluxo de tráfego urbano para reduzir congestionamentos. Imaginemos um cenário onde a prefeitura está estudando a redistribuição de pistas nas ruas principais para melhorar o fluxo de veículos. Para tal, fizeram uma análise dos dados de tráfego utilizando big data e inteligência artificial, e decidiram dividir a capacidade total das pistas de uma rua em porções que correspondem a diferentes períodos do dia, para entender melhor como esses períodos afetam o tráfego. Você foi designado para criar um programa que simule essa divisão. Sua tarefa é: Pedir ao usuário que insira a capacidade total em veículos que a rua suporta. Em seguida, solicitar que insira o número de períodos em que essa capacidade será dividida. O programa deve calcular quantos veículos pode trafegar na pista em cada período de tempo, e deve calcular também quantos veículos 'sobram' para serem distribuídos entre esses períodos. Finalmente, exiba esses dois resultados ao usuário.

# Digite a capacidade total de veículos que a rua suporta: 100
# Digite o número de períodos em que a capacidade será dividida: 10
# Veículos por período: 10
# Veículos sobrando: 0

total_veiculos = int(input("Digite a capacidade total de veículos que a rua suporta: "))
capacidade = int(input("Digite o número de períodos em que a capacidade será dividida: "))
veiculo_por_periodo = total_veiculos / capacidade
print(f"Veículos por período: {total_veiculos / capacidade}\nVeículos sobrando: {total_veiculos % capacidade}")