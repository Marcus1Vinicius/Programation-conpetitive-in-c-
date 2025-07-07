# Com a pandemia de COVID-19, muitas cidades no mundo observaram uma redução significativa no tráfego urbano durante os lockdowns. Isso levou urbanistas a repensarem o planejamento urbano, enfatizando a importância de espaços que promovam a mobilidade sustentável. Considerando a crescente demanda por alternativas de transporte saudáveis, elabore um programa que avalie um plano de mobilidade sustentável com base em dois fatores importantes: a quantidade de ruas dedicadas a pedestres e ciclistas, e a redução prevista de uso de automóveis. O programa deve receber como entrada a quantidade percentual de espaço urbano dedicado a pedestres e ciclistas e a estimativa percentual de redução no uso de automóveis. Em seguida, verifique a viabilidade do plano usando as seguintes condições: Se o espaço dedicado a pedestres e ciclistas for menor que 20% e a redução de automóveis for menor que 10%, o plano é 'Insatisfatório'. Se o espaço for entre 20% e 50% ou a redução de automóveis for entre 10% e 30%, o plano é 'Razoável'. Se o espaço for maior que 50% ou a redução de automóveis for maior que 30%, o plano é 'Ótimo'. Caso ambas as condições excedam os valores mencionados anteriormente para 'Ótimo', o plano é 'Exemplar'. Exiba uma mensagem formatada informando a viabilidade do plano como segue: 'O plano de mobilidade é [classificacao].'.



# Digite a porcentagem de espaço urbano dedicado a pedestres e ciclistas: 15.0
# Digite a estimativa percentual de redução no uso de automóveis: 5.0
# O plano de mobilidade é Insatisfatório.

# percentual pedestres e ciclistas:
# insatisfatorio: menos de 20
# razoavel: entre 20 e 50
# otimo: maior que 50

# percentual carros:
# insatisfatorio: menos de 10
# razoavel: entre 10 e 30
# otimo: acima de 30

plano_pedestre_cliclistas = float(input("Digite a porcentagem de espaço urbano dedicado a pedestres e ciclistas: "))

plano_automoveis = float(input("Digite a estimativa percentual de redução no uso de automóveis: "))

if plano_pedestre_cliclistas < 20:
    status_pedestres_ciclistas = "Plano insatisfatório"

if plano_pedestre_cliclistas > 50:
    status_pedestres_ciclistas = "Plano otimo"

else:
    status_pedestres_ciclistas = "Plano razoavel"

if plano_automoveis < 10:
    status_automoveis = "Insatisfatório"

if plano_automoveis > 30:
    status_automoveis = "Ótimo"

else:
    status_automoveis = "razoavel"