# Com a Indústria 4.0, a manutenção preditiva tornou-se vital nas indústrias, especialmente aquelas com maquinário crítico como as de petróleo e gás. Considere um sistema que monitora a temperatura e a vibração de máquinas. Uma temperatura abaixo de 60°C é considerada 'Normal', entre 60°C e 80°C como 'Atento', e acima de 80°C como 'Crítico'. Já uma vibração abaixo de 15 mm/s é 'Normal', entre 15 mm/s e 20 mm/s é 'Atento', e acima de 20 mm/s é 'Crítico'. Escreva um programa que receba a temperatura (em °C) e a vibração (em mm/s) de uma máquina como entradas do usuário e exiba o estado da máquina de acordo com a leitura de cada sensor, no formato: A máquina está em estado [estado de temperatura] para temperatura e [estado de vibração] para vibração.



# Digite a vibração da máquina em mm/s: 14.9
# A máquina está em estado Normal para temperatura e Normal para vibração.

# temperatura:
# normal : 6abaixo de 60
# atento: entre 60 e 80
# crítico : acima de 80

# vibração:
# normal : abaixo de 15mm/s
# atento: entre 15 e 20
# crítico: acima de 20

temperatura = float(input("Digite a temperatura da máquina em °C: "))

vibracao = float(input("Digite a vibração da máquina em mm/s: "))


if vibracao < 15:
    vibracao_status = " e Normal para vibração"

elif vibracao > 20:
    vibracao_status = " e crítico para vibração"

else:
    vibracao_status = " e Atento para vibração"

if temperatura < 60:
    temperatura_status = "A máquina está em estado Normal para temperatura"

if temperatura > 80:
    temperatura_status = "A máquina está em estado Crítico para temperatura"

else:
    temperatura_status = "A máquina está em estado Atento para temperatura"

print(temperatura_status + vibracao_status)


# if vibracao < 15 and temperatura < 60:
#     print("A máquina está em estado Normal para temperatura e Normal para vibração.")

# elif vibracao > 20 and temperatura > 80:
#     print("A máquina está em estado crítico para temperatura e crítico para vibração.")

