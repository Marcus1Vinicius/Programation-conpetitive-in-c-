# Num esforço para promover a adoção de tecnologias de energia renovável, um determinado governo está considerando lançar uma iniciativa que planeja subsidiar parcialmente o custo de aquisição de painéis solares para residentes de áreas rurais. A intenção é estimular a transição de combustíveis fósseis para fontes de energia mais sustentáveis. Estima-se que o custo médio para a instalação dos painéis solares é dado por uma função quadrática da forma: C(x) = 0.01x² + 10x + 2000, onde x representa a quantidade de metros quadrados de painéis solares necessários para abastecer uma propriedade. O governo propõe cobrir 25% do custo total. Escreva um programa que recebe como entrada um número inteiro positivo representando o valor de x, correspondente à área de painéis solares necessária, e retorna o valor do subsídio que o governo deve conceder.

# Digite a quantidade de metros quadrados de painéis solares necessária: 50
# O valor do subsídio que o governo deve conceder é: 631.25

x = int(input("Digite a quantidade de metros quadrados de painéis solares necessária: "))
formula = (0.01 * (x**2) + (10*x + 2000)) * 0.25
print("O valor do subsídio que o governo deve conceder é:", formula)