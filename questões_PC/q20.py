# Em uma cidade grande, o uso crescente de aplicativos de transporte por demanda está transformando a maneira como as pessoas se deslocam, oferecendo alternativas mais convenientes e rápidas. No entanto, isso também contribui para o aumento do tráfego urbano, já que mais veículos estão transitando nas ruas. As autoridades enfrentam o desafio de equilibrar a inovação tecnológica com a necessidade de reduzir congestionamentos e emissões de poluentes na atmosfera. Considere que uma agência de monitoramento de tráfego quer calcular o total de viagens feitas por veículos de aplicativos ao longo de uma semana para entender o impacto no trânsito. Desenvolva um programa que receba, para cada um dos 7 dias da semana, o número de viagens realizadas por aplicativos de transporte. Ao final, o programa deve exibir o total de viagens realizadas durante toda essa semana.


# 10
# 10
# 10
# 10
# 10
# 10
# 10
# Total de viagens na semana: 70

contador = 0

for i in range(7):
    qtd_viagens_do_dia = int(input(" "))
    contador = contador + qtd_viagens_do_dia
print(f"Total de viagens na semana: {contador}")