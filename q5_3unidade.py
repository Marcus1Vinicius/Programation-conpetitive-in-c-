# Com o avanço da Internet das Coisas (IoT), sensores industriais agora estão conectados a redes que permitem análises preditivas e manutenção remota. Em setores como o de energia, isso é usado para monitorar e ajustar o desempenho de turbinas eólicas em tempo real, maximizando a eficiência energética e reduzindo a necessidade de intervenções físicas em locais de difícil acesso. Imagine que uma empresa de energia está monitorando turbinas eólicas e precisa ajustar a posição ideal para maximizar a produção com base na velocidade do vento. A relação entre a produção de energia (P) e a velocidade do vento (v) é dada por uma equação de segundo grau: P(v) = av^2 + bv + c, onde a, b e c são constantes. Escreva um programa que solicite ao usuário a velocidade do vento em metros por segundo, e calcule a produção de energia esperada com base nos coeficientes a = 0.5, b = 3, e c = 0.

# Digite a velocidade do vento em metros por segundo: 10
# Produção de energia esperada: 80.0

v = int(input("Digite a velocidade do vento em metros por segundo: "))

print(f"Produção de energia esperada: {(0.5 * v**2) + 3*v + 0}")