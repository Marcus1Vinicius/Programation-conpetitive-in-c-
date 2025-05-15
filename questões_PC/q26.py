# Uma geladeira moderna registra automaticamente sua temperatura interna várias vezes ao longo do dia. Você foi chamado para ajudar a identificar possíveis falhas no sistema de refrigeração, como quando a temperatura sobe ou desce muito em relação ao normal.

# Para isso, você deverá desenvolver um programa que leia uma sequência de temperaturas digitadas pelo usuário. As medições devem continuar sendo registradas até que o valor "000" seja digitado, o que indica o fim da entrada. Ao finalizar, o programa deve calcular a média de todas as temperaturas informadas. Em seguida, deve identificar quais temperaturas estão muito distantes da média, considerando como fora do padrão qualquer valor que esteja mais de 20% acima ou abaixo dessa média.

# Ao final, o sistema deve mostrar a média geral de temperaturas e destacar quais valores foram considerados fora do padrão.

# Digite a temperatura (ou 000 para encerrar): 10
# Digite a temperatura (ou 000 para encerrar): 20
# Digite a temperatura (ou 000 para encerrar): 15
# Digite a temperatura (ou 000 para encerrar): 3
# Digite a temperatura (ou 000 para encerrar): 12
# Digite a temperatura (ou 000 para encerrar): 000

# Média das temperaturas: 12.00 °C
# Temperaturas fora do padrão: [20.0, 15.0, 3.0]

lista_temperaturas = []
temperaturas_fora_padrao = []

while True:
    temperatura = float(input("Digite a temperatura (ou 000 para encerrar): "))

    if temperatura == 000: 
        break

    else: 
        lista_temperaturas.append(temperatura)

media = sum(lista_temperaturas) / len(lista_temperaturas)

for i in lista_temperaturas:
    if i != media:
        temperaturas_fora_padrao.append(i)  

print(f"Média das temperatura: {media} °C \nTemperaturas fora do padrão {temperaturas_fora_padrao}") 

