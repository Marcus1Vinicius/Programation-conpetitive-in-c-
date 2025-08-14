# Desenvolva um programa que calcule a eficiência do uso de recursos em um projeto. O programa deve receber como entrada, via input do usuário, quatro valores: o orçamento total do projeto (um número real), o custo total de recursos utilizados até o momento (um número real), o número total de horas trabalhadas pela equipe (um número inteiro) e o número de tarefas concluídas (um número inteiro). A eficiência é definida como a razão entre o valor das tarefas concluídas e o custo dos recursos utilizados, multiplicada pelo total de horas trabalhadas. Considere que cada tarefa concluída adiciona um valor fixo de R$500 ao projeto. O programa deve calcular e exibir a eficiência do uso de recursos, garantindo que os custos não excedam o orçamento total. Se o custo de recursos já tiver excedido o orçamento, o programa deve informar que o projeto está ineficiente.

orcamento = float(input("Digite o orçamento total do projeto: "))
custo_total = float(input("Digite o custo total de recursos utilizados até o momento: "))
total_horas = int(input("Digite o número total de horas trabalhadas pela equipe: "))
tarefa_concluidas = int(input("Digite o número de tarefas concluídas: "))
                        
formula = ((500 * tarefa_concluidas) / custo_total) * total_horas

eficiencia = orcamento - custo_total

if eficiencia >= 0:
    print(f"Eficiência do uso de recursos: {formula}")

else:
    print("O projeto está ineficiente, pois o custo de recursos excedeu o orçamento.")
