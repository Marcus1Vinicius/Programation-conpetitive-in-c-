# Na indústria alimentícia, sensores industriais são utilizados para garantir a qualidade e segurança dos produtos. Eles podem detectar contaminantes, monitorar níveis de umidade e controlar a temperatura durante o processamento e armazenamento dos alimentos. Isso não apenas ajuda a atender às regulamentações de segurança alimentar, mas também otimiza o prazo de validade dos produtos. Considere que uma fábrica de alimentos utiliza sensores para monitorar a umidade interna de diferentes lotes de produtos em tempo real. No final do dia, é necessário realizar um cálculo para exibir um resumo aos gestores. Esse resumo deve mostrar quantos lotes estão dentro da umidade ideal, acima dela, e o produto da potência da média da umidade ao quadrado por uma constante de eficiência considerada, que pode variar. Para este problema, receba a soma total da umidade de todos os lotes, o número total de lotes em um dia, a constante de eficiência, e o valor da umidade ideal. Calcule o valor da média da umidade de cada lote e seu quadrado elevado à constante de eficiência, apresentando este valor no relatório diário. Além disso, determine e exiba quantos lotes estão dentro da umidade ideal e quantos estão acima dela.​

# Digite a soma total da umidade de todos os lotes: 480
# Digite o número total de lotes: 12
# Digite a constante de eficiência: 1.8
# Digite o valor da umidade ideal: 40
# Média da umidade ao quadrado multiplicada pela constante de eficiência: 2880.0
# Lotes dentro da umidade ideal: 12
# Lotes acima da umidade ideal: 0

soma_total_umidade = int(input("Digite a soma total da umidade de todos os lotes: "))
total_lotes = int(input("Digite o número total de lotes: "))
print(total_lotes)
constante_eficiencia = float(input("Digite a constante de eficiência: "))
umidade_ideal = int(input("Digite o valor da umidade ideal: "))
media_umidade = (umidade_ideal**2) * constante_eficiencia

for i in total_lotes:
    umidade_lote = int(input("Digite a umidade do lote ", i , ": "))
    if(umidade_lote > umidade_ideal):
        contador_umidade_acima = contador_umidade_acima + 1
    elif(umidade_lote == umidade_ideal):
        contador_umidade_ideal = contador_umidade_ideal + 1
print("Média da umidade ao quadrado multiplicada pela constante de eficiência: ",media_umidade, "Lotes dentro da umidade ideal: ", contador_umidade_ideal, "Lotes acima da umidade ideal: ", contador_umidade_acima)

