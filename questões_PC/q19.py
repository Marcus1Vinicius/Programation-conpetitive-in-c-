# Nos esforços para melhorar o atendimento em cidades menores com infraestrutura bancária limitada, uma nova iniciativa foi proposta: a implementação de centrais comunitárias com caixas eletrônicos que permitem aos moradores realizar operações básicas. No contexto dessa iniciativa, você foi encarregado de criar um programa simples para o caixa eletrônico comunitário que funcione da seguinte forma: ele deve permitir que um usuário insira quantos saques quiser e, cada vez que uma quantia for sacada, o sistema deve solicitar o valor do próximo saque. O programa deve parar de solicitar valores quando o usuário inserir um valor de saque igual a qualquer número negativo, o que deve ser considerado como um sinal para encerrar o processo de saque. Após o término, o programa deve exibir a maior quantia sacada. Desenvolva o programa cujo fluxo se comporta conforme descrito, garantindo que o usuário possa inserir valores até decidir parar.

# Digite o valor do saque (ou um número negativo para encerrar): 10
# Digite o valor do saque (ou um número negativo para encerrar): 20
# Digite o valor do saque (ou um número negativo para encerrar): 30
# Digite o valor do saque (ou um número negativo para encerrar): -1
# A maior quantia sacada foi: 30

contador = 0 

while True:
    valor_saque = float(input("Digite o valor do saque (ou um número negativo para encerrar): "))

    if valor_saque == -1:
        break

    elif valor_saque > contador:
        
        contador = valor_saque

print("A maior quantia sacada foi: ", contador)