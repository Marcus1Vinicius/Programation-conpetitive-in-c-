# Em uma empresa de logística, os entregadores precisam saber qual rota seguir com base na distância e no tipo de carga. Cada rota tem um conjunto específico de instruções.

# Escreva um programa que receba dois inteiros: a distância em quilômetros e o tipo de carga (1 para frágil e 2 para não frágil).

# A rota deve ser escolhida de acordo com as seguintes regras:

# - Se a distância for igual ou menor a 30 km, verifique o tipo de carga:

#   - Se a carga for frágil, imprima 'Rota A'.

#   - Se a carga não for frágil, imprima 'Rota B'.

# - Se a distância for superior a 30 km, verifique novamente o tipo de carga:

#   - Se a carga for frágil, imprima 'Rota C'.

#   - Se a carga não for frágil, imprima 'Rota D'.



# Digite a distância da entrega: 60
# Digite o tipo de carga a ser entregue: 1
# Siga pela:
# Rota C

distancia = int(input("Digite a distância da entrega: "))
tipo_carga = int(input("Digite o tipo de carga a ser entregue: "))

if distancia > 30:
    if tipo_carga == 1:
        print("Rota C")
    elif tipo_carga == 2:
        print("Rota D")
else:
    if tipo_carga == 1:
        print("Rota A")
    if tipo_carga == 2:
        print("Rota B")