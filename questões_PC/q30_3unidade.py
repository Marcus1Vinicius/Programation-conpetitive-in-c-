# No bairro de Santa Clara, um novo aplicativo foi lançado para otimizar as rotas dos entregadores de bicicleta. Este aplicativo utiliza inteligência artificial para analisar dados de trânsito em tempo real e prever as melhores rotas, levando em consideração possíveis bloqueios de ruas e condições meteorológicas. Os entregadores agora conseguem reduzir significativamente o tempo de entrega e aumentar suas diárias. Para ajudar a calcular o tempo de entrega estimado, deseja-se uma função que estime essa duração em minutos. Para isso, considere que a bicicleta se desloca a uma velocidade média de 15 km/h. O aplicativo deve solicitar o total de quilômetros da rota ao entregador via input() e então calcular o tempo estimado de entrega com base na velocidade média mencionada. Escreva uma função que não recebe parâmetros, mas solicita a informação da rota diretamente ao entregador e retorna o tempo de entrega estimado em minutos.

# Digite o total de quilômetros da rota: 30
# Tempo estimado de entrega: 120.0 minutos

def duracao():
    km = int(input("Digite o total de quilômetros da rota: "))
    formula = (km / 15) * 60
    return formula

resultado = duracao()

print(f"Tempo estimado de entrega: {resultado} minutos")
