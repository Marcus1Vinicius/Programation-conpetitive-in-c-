# ​A empresa de logística deseja implementar um sistema automatizado para calcular a comissão dos motoristas com base no número de pacotes entregues e na distância percorrida. A comissão de um motorista é calculada seguindo as regras abaixo:

# 1. Para cada pacote entregue, o motorista recebe R$2.
# 2. Além disso, é pago R$0.50 por cada quilômetro percorrido.

# Escreva uma função chamada `calcular_comissao` que receba como entrada o número de pacotes entregues e a distância total percorrida em quilômetros, recebidos por input do usuário. A função deve retornar o valor total da comissão a ser paga ao motorista.

# Quantos pacotes foram entregues? 10
# Qual a distância percorrida (em km)? 20
# Comissão total: 30.0


def calcular_comissao(qtd_pacotes, distancia):

    pagamento = (qtd_pacotes * 2) + (distancia * 0.50)

    return pagamento

numero_pacotes = int(input("Quantos pacotes foram entregues? "))

km_rodados = float(input("Qual a distância percorrida (em km)? "))

resultado = calcular_comissao(numero_pacotes, km_rodados)

print(f"Comissão total: {resultado}")
