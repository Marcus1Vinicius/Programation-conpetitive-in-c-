# Durante a pandemia, as filas em bancos se tornaram um ponto crítico de preocupação, uma vez que o distanciamento social era essencial para a saúde pública. Muitos bancos implementaram medidas rigorosas, como limites de ocupação dentro das agências e marcações no chão para assegurar a distância necessária entre as pessoas. Adicionalmente, incentivaram o uso de plataformas online para transações e consultas, reduzindo a necessidade de comparecimento físico dos clientes. No contexto de um banco, você foi encarregado de criar uma ferramenta para ajudar a gerenciar a fila de atendimento. Crie uma função que calcula o tempo estimado de espera para um cliente na fila. A função deve receber como parâmetros o número total de clientes na fila (inteiro), a média de tempo de atendimento por cliente em minutos (float), e um fator de ajuste (float) que considera possíveis atrasos. Caso o fator de ajuste não seja passado como argumento, utilize o valor padrão de 1.1, que considera um atraso de 11%. Além disso, sua função deve interagir com o usuário perguntando a média de tempo de atendimento e o número de clientes na fila. No final, imprima o tempo estimado até que o cliente recém chegado seja atendido.

# Quantos clientes estão na fila? 15
# Qual é a média de tempo de atendimento por cliente (em minutos)? 25
# Deseja informar um fator de ajuste? (pressione Enter para usar o valor padrão 1.1): 1.5
# Tempo estimado de espera: 562.50 minutos

def tempo_espera(qtd_clientes, media_atendimento, ajuste):

    formula = (qtd_clientes * media_atendimento) * ajuste

    return formula 

clientes = int(input("Quantos clientes estão na fila? "))

tempo_atendimento = float(input("Qual é a média de tempo de atendimento por cliente (em minutos)? "))

input_ajuste = input("Deseja informar um fator de ajuste? (pressione Enter para usar o valor padrão 1.1): ")

if input_ajuste.strip() == "":
    atraso = 1.1

else:
    atraso = float(input_ajuste)

resultado = tempo_espera(clientes, tempo_atendimento, atraso)

print(f"Tempo estimado de espera: {resultado} minutos")