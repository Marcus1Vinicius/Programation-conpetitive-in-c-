# Uma fábrica de brinquedos produz carrinhos diariamente. O custo de produção (C) em reais por dia é dado pela função de primeiro grau C(x) = 50x + 200, onde x é o número de carrinhos produzidos em um dia. Além disso, a receita (R) obtida pela venda desses carrinhos é dada pela função de primeiro grau R(x) = 70x.

# A diretoria deseja saber o lucro do dia, que é calculado pela diferença entre a receita e o custo de produção.

x = int(input("Digite a quantidade de carrinhos produzidos no dia: "))

c = (50*x) + 200

r = 70 * x

lucro = r - c

print(f'Lucro do dia: R$ {lucro}')